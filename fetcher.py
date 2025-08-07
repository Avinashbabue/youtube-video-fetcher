import os
import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import Video

# Read all API keys from environment variable (comma-separated) and filter out empty strings
API_KEYS = [k for k in os.getenv("YOUTUBE_API_KEY", "").split(",") if k]

# Read search query from environment variable
SEARCH_QUERY = os.getenv("YOUTUBE_SEARCH_QUERY")
if not SEARCH_QUERY:
    raise ValueError("Missing YOUTUBE_SEARCH_QUERY in .env")

def get_youtube_service(api_key):
    """
    Create a YouTube Data API service object using the given API key.
    """
    return build("youtube", "v3", developerKey=api_key)

def fetch_latest_videos(db: Session):
    """
    Fetch latest videos from YouTube for the given search query and store them in the database.
    Videos published within the last 10 minutes are considered.
    """
    # Calculate time window: videos published after this timestamp will be fetched
    published_after = (datetime.utcnow() - timedelta(minutes=10)).isoformat("T") + "Z"
    latest_response = None

    # Try fetching data using each API key until one works
    for api_key in API_KEYS:
        youtube = get_youtube_service(api_key)
        try:
            # Create request to YouTube Search API
            request = youtube.search().list(
                q=SEARCH_QUERY,
                type="video",
                order="date",
                part="snippet",
                maxResults=10,
                publishedAfter=published_after
            )
            latest_response = request.execute()  # Execute API request
            break  # Stop if request succeeds
        except HttpError as e:
            logging.warning(f"API key failed: {api_key} ({e})")
            # If quota exceeded, try the next API key
            if "quotaExceeded" in str(e) or "dailyLimitExceeded" in str(e):
                continue
            else:
                raise  # Raise error if it's not quota-related
    else:
        # If all API keys failed
        logging.error("All API keys exhausted or failed.")
        return

    new_videos = []
    # Process each video in the API response
    for item in latest_response.get("items", []):
        video_id = item["id"].get("videoId")
        snippet = item.get("snippet", {})

        # Skip if required fields are missing
        if not video_id or not all(k in snippet for k in ("title", "description", "publishedAt", "thumbnails")):
            continue

        # Extract required details
        title = snippet["title"]
        description = snippet["description"]
        published_at = snippet["publishedAt"]
        thumbnail_url = (
            snippet["thumbnails"].get("high", snippet["thumbnails"].get("default", {})).get("url", "")
        )

        # Add to list only if video is not already in the database
        if not db.query(Video).filter_by(video_id=video_id).first():
            try:
                video = Video(
                    video_id=video_id,
                    title=title,
                    description=description,
                    published_at=datetime.fromisoformat(published_at.replace("Z", "+00:00")),
                    thumbnail_url=thumbnail_url
                )
                new_videos.append(video)
            except Exception as data_exc:
                logging.warning(f"Skipping video {video_id} due to data error: {data_exc}")

    # Insert new videos into the database
    try:
        if new_videos:
            db.add_all(new_videos)
            db.commit()
            logging.info(f"Inserted {len(new_videos)} new videos.")
        else:
            logging.info("No new videos found.")
    except Exception as db_exc:
        db.rollback()  # Rollback if any database error occurs
        logging.error(f"Database error: {db_exc}")
