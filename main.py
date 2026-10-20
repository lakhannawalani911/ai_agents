from google import genai
from os import environ
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model= environ.get("GEMINI_MODEL_NAME"),
    contents="explain AI agent in 10 words.",
)
print(response.text)