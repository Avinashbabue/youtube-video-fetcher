# 🎥 YouTube Video Fetcher API
# A Python-based API to fetch and store YouTube video details.

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
  - step: "Step 1: Clone the Repository"
    command: |
      git clone https://github.com/your-username/youtube-video-fetcher.git
      cd youtube-video-fetcher
      
  - step: "Step 2: Create a Virtual Environment (Windows)"
    command: |
      python -m venv venv
      venv\Scripts\activate

  - step: "Step 3: Install Dependencies"
    command: |
      pip install -r requirements.txt

  - step: "Step 4: Configure Environment Variables"
    command: |
      cp .env.example .env
    note: |
      Edit `.env` and set:
      YOUTUBE_API_KEY=your_api_key_here
      DATABASE_URL=sqlite:///videos.db

run_api_server:
  step: "Step 5: Run the API Server"
  command: |
    uvicorn main:app --reload
  url:
    - API: http://127.0.0.1:8000
    - Docs: http://127.0.0.1:8000/docs

run_dashboard:
  step: "Step 6: Run the Dashboard"
  command: |
    streamlit run dashboard.py
  url:
    - Dashboard: http://localhost:8501
