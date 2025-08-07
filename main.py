from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from apscheduler.schedulers.background import BackgroundScheduler
from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime
import logging
import os

from database import SessionLocal, engine, Base
from models import Video
from fetcher import fetch_latest_videos

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# Database Setup
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI(title="YouTube Video Fetcher")

# Pydantic Response Model
class VideoResponse(BaseModel):
    video_id: str
    title: str
    description: str
    published_at: datetime
    thumbnail_url: str

    model_config = ConfigDict(from_attributes=True)  # Pydantic v2 equivalent of orm_mode

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# APScheduler Setup
scheduler = BackgroundScheduler()

def scheduled_video_fetch():
    db = SessionLocal()
    try:
        logger.info("Fetching latest videos (scheduler)...")
        fetch_latest_videos(db)
        logger.info("Video fetch complete (scheduler).")
    except Exception as e:
        logger.exception("Error during scheduled video fetch: %s", str(e))
    finally:
        db.close()

@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(scheduled_video_fetch, "interval", seconds=10)
    scheduler.start()
    logger.info("Scheduler started, running every 10 seconds.")

@app.on_event("shutdown")
def shutdown_scheduler():
    scheduler.shutdown(wait=True)
    logger.info("Scheduler shut down.")

# API Routes
@app.get("/videos", response_model=List[VideoResponse])
def get_videos(
    skip: int = Query(0, ge=0, description="Number of videos to skip"),
    limit: int = Query(10, le=50, description="Max number of videos to return"),
    db: Session = Depends(get_db)
):
    try:
        videos = (
            db.query(Video)
            .order_by(desc(Video.published_at))
            .offset(skip)
            .limit(limit)
            .all()
        )
        return videos 
    except Exception as e:
        logger.exception("Failed to fetch videos: %s", str(e))
        raise HTTPException(status_code=500, detail=str(e))


