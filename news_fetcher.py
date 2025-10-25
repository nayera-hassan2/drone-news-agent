# news_fetcher.py
import requests
from bs4 import BeautifulSoup

def fetch_article_image(url):
    """
    Fetch the first image from the article page using the og:image meta tag.
    """
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            return og_image["content"]
    except Exception as e:
        print(f"Could not fetch image from {url}: {e}")
    return None

def fetch_news(keyword="drone India", max_articles=5):
    """
    Fetch latest news articles from Google News RSS.
    Returns a list of dictionaries with title, link, publication date, and image.
    """
    url = f"https://news.google.com/rss/search?q={keyword}&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml-xml")

    items = soup.find_all("item")[:max_articles]
    articles = []

    for item in items:
        title = item.title.text
        link = item.link.text
        pubDate = item.pubDate.text

        # Try RSS image first
        image = None
        media_thumbnail = item.find("media:thumbnail")
        media_content = item.find("media:content")
        if media_thumbnail and media_thumbnail.get("url"):
            image = media_thumbnail["url"]
        elif media_content and media_content.get("url"):
            image = media_content["url"]

        # If no RSS image, fetch from article page
        if not image:
            image = fetch_article_image(link)

        articles.append({
            "title": title,
            "link": link,
            "pubDate": pubDate,
            "image": image
        })

    return articles

# Test the function
if __name__ == "__main__":
    news_list = fetch_news()
    for i, n in enumerate(news_list, 1):
        print(f"Article {i}:")
        print(f"Title: {n['title']}")
        print(f"Link: {n['link']}")
        print(f"Published Date: {n['pubDate']}")
        print(f"Image: {n['image']}")
        print("-" * 50)
