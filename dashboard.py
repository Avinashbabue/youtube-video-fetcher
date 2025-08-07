# dashboard.py
import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "videos.db"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM videos", conn)
    conn.close()
    return df

st.set_page_config(page_title="YouTube Video Dashboard", layout="wide")
st.title("📺 YouTube Video Dashboard")

df = load_data()

if df.empty:
    st.warning("No videos found in the database.")
    st.stop()

# Convert published date
df["published_at"] = pd.to_datetime(df["published_at"])

# Sidebar filters
st.sidebar.header("🔍 Filters")
date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["published_at"].min().date(), df["published_at"].max().date()]
)
sort_by = st.sidebar.selectbox(
    "Sort by",
    options=["published_at", "title"],
    index=0
)
sort_order = st.sidebar.radio("Sort order", ["Descending", "Ascending"], index=0)

# Apply date filter
filtered_df = df.copy()
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df["published_at"].dt.date >= start_date)
        & (filtered_df["published_at"].dt.date <= end_date)
    ]

# Sorting
filtered_df = filtered_df.sort_values(
    by=sort_by,
    ascending=(sort_order == "Ascending")
)

st.success(f"Found {len(filtered_df)} videos")

# Function to make clickable video link
def make_clickable(video_id, text):
    url = f"https://www.youtube.com/watch?v={video_id}"
    return f'<a href="{url}" target="_blank">{text}</a>'

# Create video link column
filtered_df["video_link"] = filtered_df.apply(
    lambda row: make_clickable(row["video_id"], row["title"]), axis=1
)

# Add thumbnail HTML
filtered_df["thumbnail"] = filtered_df["thumbnail_url"].apply(
    lambda url: f'<img src="{url}" width="120">'
)

# Display table
st.write(
    filtered_df[["thumbnail", "video_link", "published_at"]]
    .to_html(escape=False, index=False),
    unsafe_allow_html=True
)
