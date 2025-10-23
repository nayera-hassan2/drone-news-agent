# main.py
from news_fetcher import fetch_news

# For actual usage with your own OpenAI API key, uncomment this line:
# from summarizer import summarize_article

# For testing/demo purposes (no API key required), use this:
from summarizer_test import summarize_article

from formatter import format_post
from poster import post_to_social_media


def run_daily_agent():
    print("Running Daily AI Agent...")
    articles = fetch_news()
    for article in articles:
        summary = summarize_article(article.get("title") + " " + article.get("link"))
        post = format_post(summary, article.get("link"))
        post_to_social_media(post)

# Test
if __name__ == "__main__":
    run_daily_agent()
