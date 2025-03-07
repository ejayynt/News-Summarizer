import time
import requests
from langchain_mistralai import ChatMistralAI
from langchain.memory import ConversationBufferMemory
from config import MISTRAL_API_KEY, NEWS_API_KEY

# ✅ Initialize Mistral AI Model
llm = ChatMistralAI(model_name="open-mistral-7b", mistral_api_key=MISTRAL_API_KEY)

# ✅ Memory for Conversations (Optional, not used much here)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


def fetch_news(category="technology"):
    """Fetch the latest news articles from NewsAPI."""
    url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("articles", [])

    return []


def summarize_text(text):
    """Summarize a single news article using Mistral AI."""
    try:
        prompt = f"Summarize this news article:\n{text}"
        return llm.predict(prompt)
    except Exception as e:
        return f"Error summarizing article: {e}"


def fetch_and_summarize_news(category="technology"):
    """Fetch news and summarize each article separately to avoid rate limits."""
    news_articles = fetch_news(category)  # Get latest news
    summarized_news = []

    for idx, article in enumerate(news_articles):
        content = article.get("content", "")

        if not content:
            summary = "No content available"
        else:
            # ✅ Call the API separately for each article
            summary = summarize_text(content)

        summarized_news.append(
            {"title": article["title"], "summary": summary, "url": article["url"]}
        )

        # ✅ OPTIONAL: Add a short delay to prevent rate limiting
        time.sleep(1.5)  # Adjust based on rate limit behavior

    return summarized_news
