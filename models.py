from sqlalchemy import Column, String, DateTime
from database import Base

class Video(Base):
    """
    SQLAlchemy model for storing YouTube video metadata.
    """
    __tablename__ = "videos"

    video_id = Column(String(64), primary_key=True, index=True)
    title = Column(String(512))
    description = Column(String)
    published_at = Column(DateTime, index=True)
    thumbnail_url = Column(String(1024))