import streamlit as st
from agent import fetch_and_summarize_news

st.title("📰 AI-Powered News Summarizer")

# Fetch and display news on startup
with st.spinner("Fetching and summarizing the latest news..."):
    news = fetch_and_summarize_news()

# Display summarized news
for idx, article in enumerate(news):
    st.subheader(f"{idx + 1}. {article['title']}")
    st.write(f"**Summary:** {article['summary']}")
    st.markdown(f"[Read more]({article['url']})")
    st.markdown("---")
