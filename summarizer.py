# summarizer.py
import os
from dotenv import load_dotenv
import openai
import re

# Load API key
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

openai.api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key Loaded:", bool(openai.api_key))  # Should print True

def extract_keywords(text, top_n=5):
    """
    Simple keyword extraction: pick most frequent non-stopwords.
    """
    stopwords = set([
        "the", "and", "of", "in", "a", "to", "for", "with", "on", "is",
        "as", "are", "by", "an", "be", "from", "at", "that", "this", "it"
    ])
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}
    for word in words:
        if word not in stopwords and len(word) > 3:
            freq[word] = freq.get(word, 0) + 1
    sorted_keywords = sorted(freq, key=freq.get, reverse=True)
    return sorted_keywords[:top_n]

def generate_hashtags(keywords):
    return [f"#{k.capitalize()}" for k in keywords]

def summarize_article(text, max_length=200):
    """
    Summarize text into 2–3 paragraphs and extract hashtags/keywords.
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize this article in 2-3 paragraphs:\n\n{text}"}],
        max_tokens=max_length
    )
    summary = response.choices[0].message.content

    keywords = extract_keywords(text)
    hashtags = generate_hashtags(keywords)

    return {
        "summary": summary,
        "keywords": keywords,
        "hashtags": hashtags
    }

# Test
if __name__ == "__main__":
    sample_text = "Drones are rapidly changing delivery services across India, with companies testing UAV technology for faster and safer shipments."
    result = summarize_article(sample_text)
    print("Summary:", result["summary"])
    print("Keywords:", result["keywords"])
    print("Hashtags:", result["hashtags"])
