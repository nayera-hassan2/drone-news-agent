# news_fetcher.py
import requests
from bs4 import BeautifulSoup

def fetch_news(keyword="drone India", max_articles=5):
    """
    Fetch latest news articles from Google News RSS.
    Returns a list of dictionaries with title, link, date, image.
    """
    url = f"https://news.google.com/rss/search?q={keyword}&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml-xml")
    items = soup.find_all("item")[:max_articles]

    articles = []
    for item in items:
        article = {
            "title": item.title.text,
            "link": item.link.text,
            "pubDate": item.pubDate.text,
            "image": None  # placeholder, RSS may not have images
        }
        articles.append(article)
    return articles

# Test the function
if __name__ == "__main__":
    news_list = fetch_news()
    for n in news_list:
        print(n)
