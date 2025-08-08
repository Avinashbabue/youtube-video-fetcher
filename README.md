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
  - step: Clone the Repository
    command: |
      ```bash
      git clone https://github.com/your-username/youtube-video-fetcher.git
      cd youtube-video-fetcher
      ```
      
  - step: Create a Virtual Environment (Windows)
    command: |
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

  - step: Create a Virtual Environment (Linux/Mac)
    command: |
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

  - step: Install Dependencies
    command: |
      ```bash
      pip install -r requirements.txt
      ```

  - step: Configure Environment Variables
    command: |
      ```bash
      cp .env.example .env
      ```
    note: Edit `.env` and set  
      ```
      YOUTUBE_API_KEY=your_api_key_here
      DATABASE_URL=sqlite:///videos.db
      ```

run_api_server:
  command: |
    ```bash
    uvicorn main:app --reload
    ```
  url:
    - API: http://127.0.0.1:8000
    - Docs: http://127.0.0.1:8000/docs

run_dashboard:
  command: |
    ```bash
    streamlit run dashboard.py
    ```
  url:
    - Dashboard: http://localhost:8501
