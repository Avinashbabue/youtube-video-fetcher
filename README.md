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
git clone https://github.com/your-username/youtube-video-fetcher.git
cd youtube-video-fetcher
```

### 2. Create a Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

- **Edit `.env` and set:**
  ```
  YOUTUBE_API_KEY=your_api_key
  YOUTUBE_SEARCH_QUERY=your_query
  ```

### 5. Run the API Server

```bash
uvicorn main:app --reload
```

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6. Run the Dashboard

```bash
streamlit run dashboard.py
```

- Dashboard: [http://localhost:8501](http://localhost:8501)

---

## 📝 Notes

- Make sure to set up your YouTube API key and search query in the `.env` file.
- For Linux/macOS, activate your virtual environment with `source venv/bin/activate`.
- The dashboard provides an interactive interface to view and filter fetched YouTube videos.

---

## 📄 License

[MIT](LICENSE)
