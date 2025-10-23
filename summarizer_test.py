# summarizer_test.py
import os
from dotenv import load_dotenv
import openai

# Load API key (optional, won't be used with mock)
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)
openai.api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key Loaded:", bool(openai.api_key))

# Mock function to simulate OpenAI summarization
def summarize_article(text, max_length=200):
    # Simulate a summary without hitting API
    return f"[MOCK SUMMARY] {text[:75]}..."

# Test
if __name__ == "__main__":
    sample_text = "Drones are rapidly changing delivery services across India..."
    print(summarize_article(sample_text))
