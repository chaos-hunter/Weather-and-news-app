# news.py
import requests
from datetime import datetime


NEWS_API_TOKEN = "YOUR API KEY"
NEWS_API_URL = "https://api.thenewsapi.com/v1/news/top"


def get_news_text(country_code):
    """
    Fetch top news headlines from TheNewsAPI for the given country_code.
    - e.g., 'us', 'ca', 'gb'

    Returns a string with the headlines.
    """
    # Format today's date for the heading
    today_str = datetime.now().strftime("%A, %B %d, %Y")

    # Build query params
    params = {
        "api_token": NEWS_API_TOKEN,
        "locale": country_code,
        "limit": 10
    }

    response = requests.get(NEWS_API_URL, params=params)
    if not response.ok:
        return f"Error fetching news: HTTP {response.status_code}"

    data = response.json()
    articles = data.get("data", [])
    if not articles:
        return f"No articles found for locale '{country_code}'."

    lines = []
    lines.append(f"Top News Headlines for {country_code.upper()}, {today_str}\n")

    for i, article in enumerate(articles, start=1):
        title = article.get("title", "Untitled")
        snippet = article.get("snippet", "")
        lines.append(f"{i}. {title}")
        if snippet:
            lines.append(f"   {snippet}\n")

    return "\n".join(lines)
