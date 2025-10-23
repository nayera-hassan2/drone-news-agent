# Drone News AI Agent

## Overview
This project automates:
1. Fetching latest drone news  
2. Summarizing articles using GPT  
3. Formatting social media posts  
4. Auto-posting to LinkedIn/Twitter  

## Folder Structure
- `news_fetcher.py` – Fetches news articles  
- `summarizer.py` – Summarizes news using OpenAI  
- `formatter.py` – Formats social media posts  
- `poster.py` – Posts content online  
- `scheduler.py` – Runs daily agent  
- `utils.py` – Helper functions  
- `screenshots/` – Screenshots for submission  

## Usage
1. Activate virtual environment  
2. Install dependencies from `requirements.txt`  
3. Fill `.env` with API keys  
4. Run `main.py` or `scheduler.py` for daily automation  

---

## ⚙️ Usage Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/drone-news-agent.git
cd drone-news-agent

2️⃣ Create and Activate a Virtual Environment
python -m venv venv

Activate the environment:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your Own OpenAI API Key
Create a .env file in the root folder (same location as main.py) and add:

OPENAI_API_KEY=your_openai_api_key_here

Tip: If your OpenAI API quota is exceeded, mock summaries are already included for testing.

5️⃣ Run the Project
To run the main script manually:

python main.py

To run it automatically on a daily schedule:

python scheduler.py

Example .env File
# Example environment variables
OPENAI_API_KEY=your_openai_api_key_here

👩‍💻 Author
Nayera Hassan
AI Automation Project | 2025







