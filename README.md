# News Summarizer
This AI-driven system combines real-time news fetching with LLM-based text summarization. This project is implemented using LangChain, Mistral AI, and Streamlit. This system is important as it automates the process of fetching the news and summarizes it to help the user know what is going on in a very concise yet insightful and efficient manner. 

## Features
* Uses [NewsAPI](https://newsapi.org) to obtain live news.
* Summarizes using [Mistral AI](https://mistral.ai/).
* A basic interface has been provided using [StreamLit](https://streamlit.io/)

## Configure API Keys
The API keys are stored in the ` config.py ` file for simplicity and ease of access.
```python
# config.py
MISTRAL_API_KEY = "your_mistral_api_key_here"
NEWS_API_KEY = "your_newsapi_key_here"
```

## Future Improvements
* Add multi-language support for summaries
* Improve news filtering using AI-powered ranking
* Integrate speech-to-text for audio summaries
