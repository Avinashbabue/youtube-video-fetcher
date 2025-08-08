# 🎥 YouTube Video Fetcher API

A Python-based API to fetch and store YouTube video details, featuring a FastAPI backend and a Streamlit dashboard for visualization.

---

## 📁 Project Structure

```
youtube-video-fetcher/
├── main.py             # FastAPI application entry point
├── fetcher.py          # Periodic video fetching logic
├── database.py         # Database setup (SQLAlchemy)
├── models.py           # Database models
├── dashboard.py        # Streamlit dashboard for viewing videos
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
```

---

## 🚀 Setup & Run

### 1. Clone the Repository

```bash
# Clone the repository from GitHub to your local machine
git clone https://github.com/your-username/youtube-video-fetcher.git

# Navigate into the project directory
cd youtube-video-fetcher
```

### 2. Create a Virtual Environment (Windows)

```bash
# Create a virtual environment named 'venv' for dependency isolation
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install all required Python packages from requirements.txt
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Create a new .env file in the project root by copying the contents of .env.example manually
```

- **Edit `.env` and set your configuration:**
  ```
  YOUTUBE_API_KEY=your_api_key      # Your YouTube Data API v3 key
  YOUTUBE_SEARCH_QUERY=your_query   # Search query for fetching videos
  ```

### 5. Run the API Server

```bash
# Start the FastAPI server with live reload enabled
uvicorn main:app --reload
```
- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6. Run the Dashboard

```bash
# Launch the Streamlit dashboard to view and explore the fetched videos
streamlit run dashboard.py
```
- Dashboard: [http://localhost:8501](http://localhost:8501)

---

## 📝 Notes

- Make sure to set up your YouTube API key and search query in the `.env` file.
- The dashboard provides an interactive interface to view and filter fetched YouTube videos.

---

## 📄 License

[MIT](LICENSE)
