import os
from dotenv import load_dotenv
import openai

# Ensure .env loads from current directory
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

openai.api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key Loaded:", bool(openai.api_key))  # Should print True

# Check available models
available_models = openai.Model.list()
print("Available models:", [m.id for m in available_models])

def summarize_article(text, max_length=200):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        max_tokens=max_length
    )
    summary = response.choices[0].message.content
    return summary


# Test
if __name__ == "__main__":
    sample_text = "Drones are rapidly changing delivery services across India..."
    print(summarize_article(sample_text))
