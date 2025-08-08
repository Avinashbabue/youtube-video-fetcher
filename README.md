# 🎥 YouTube Video Fetcher API
# Python-based API to fetch and store YouTube video details.

project_structure: |
  youtube-video-fetcher/
    ├── main.py             # FastAPI application entry point
    ├── fetcher.py          # Periodic video fetching logic
    ├── database.py         # Database setup (SQLAlchemy)
    ├── models.py           # Database models
    ├── dashboard.py        # Streamlit dashboard for viewing videos
    ├── requirements.txt    # Python dependencies
    ├── README.md           # Project documentation
    └── .gitignore          # Git ignore rules

setup_and_run:
  - step: 1
    name: Clone the Repository
    command: |
      git clone https://github.com/your-username/youtube-video-fetcher.git
      cd youtube-video-fetcher
      
  - step: 2
    name: Create a Virtual Environment (Windows)
    command: |
      python -m venv venv
      venv\Scripts\activate

  - step: 3
    name: Install Dependencies
    command: |
      pip install -r requirements.txt

  - step: 4
    name: Configure Environment Variables
    command: |
      cp .env.example .env
    note: |
      Edit `.env` and set:
      YOUTUBE_API_KEY=your_api_key
      YOUTUBE_SEARCH_QUERY=your_query

  - step: 5
    name: Run the API Server
    command: |
      uvicorn main:app --reload
    urls:
      - API: http://127.0.0.1:8000
      - Docs: http://127.0.0.1:8000/docs

  - step: 6
    name: Run the Dashboard
    command: |
      streamlit run dashboard.py
    urls:
      - Dashboard: http://localhost:8501
