import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Provider
PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

# Groq configuration
if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. Use groq."
    )

# Check API key
if not API_KEY:
    raise SystemExit(
        "No Groq API key found. Check your .env file."
    )

# Create Groq client
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

# Private college data
COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

# Questions for the lab
QUESTIONS = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Write a two-line welcome message for new AI students.",
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | "
        f"model: {MODEL} ===\n"
    )