name: YouTube Video Fetcher
description: |
  A FastAPI + Streamlit project to fetch the latest YouTube videos using the YouTube Data API,
  store them in a database, and view them via a dashboard.

project_structure: |
  youtube-video-fetcher/
    ├── main.py         # FastAPI application entry point
    ├── fetcher.py      # Periodic video fetching logic
    ├── database.py     # Database setup (SQLAlchemy)
    ├── models.py       # Database models
    ├── dashboard.py    # Streamlit dashboard for viewing videos
    ├── requirements.txt# Python dependencies
    ├── .env.example    # Example environment variables
    ├── README.md       # Project documentation
    └── .gitignore      # Git ignore rules

setup_and_run:
  clone_repository: |
    git clone https://github.com/Avinashbabue/youtube-video-fetcher.git
    cd youtube-video-fetcher

  create_virtualenv_windows: |
    python -m venv venv
    venv\Scripts\activate

  create_virtualenv_linux_mac: |
    python3 -m venv venv
    source venv/bin/activate

  install_dependencies: |
    pip install -r requirements.txt

  setup_env_file: |
    cp .env.example .env
    # Edit .env and add:
    # YOUTUBE_API_KEY=your_api_key_here
    # DATABASE_URL=sqlite:///videos.db

run_server: |
  uvicorn main:app --reload
  # Access API: http://127.0.0.1:8000
  # API docs: http://127.0.0.1:8000/docs

run_dashboard: |
  streamlit run dashboard.py
  # Access dashboard: http://localhost:8501

features: |
  - Fetch latest videos from YouTube channels using YouTube Data API.
  - Store video metadata in a database.
  - REST API built with FastAPI.
  - Dashboard built with Streamlit to visualize stored videos.
  - Modular and clean architecture.

tech_stack:
  backend: FastAPI
  frontend: Streamlit
  database: SQLite + SQLAlchemy
  api: YouTube Data API
  language: Python 3.x
