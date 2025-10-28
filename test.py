from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

print("GROQ_API_KEY loaded:", bool(os.getenv("GROQ_API_KEY")))
print("SERPER_API_KEY loaded:", bool(os.getenv("SERPER_API_KEY")))

