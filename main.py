# main.py
from news_fetcher import fetch_news

# For actual usage with your own OpenAI API key, uncomment this line:
# from summarizer import summarize_article

# For testing/demo purposes (no API key required), use this:
from summarizer_test import summarize_article

from formatter import format_post
from poster import post_to_social_media

def run_daily_agent():
    print("Running Daily AI Agent...\n")
    
    # Step 1: Fetch news
    articles = fetch_news(keyword="drone India", max_articles=5)
    if not articles:
        print("No articles found.")
        return

    for i, article in enumerate(articles, start=1):
        print(f"\nProcessing Article {i}: {article['title']}")
        
        # Step 2: Summarize article
        summary_info = summarize_article(article.get("title") + " " + article.get("link"))
        
        # Step 3: Format post for social media
        post_content = format_post(summary_info, article.get("link"))
        
        # Step 4: Auto-post
        post_to_social_media(post_content, image_path=article.get("image"))
        
        # Optional: Print summary and hashtags for verification
        print("Summary:", summary_info["summary"])
        print("Keywords:", summary_info["keywords"])
        print("Hashtags:", summary_info["hashtags"])
        print("Post Content:", post_content)

# Test
if __name__ == "__main__":
    run_daily_agent()
