import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_sector(sector, news):
    prompt = f"""
Analyze the {sector} market using this data:

{news}

Format answer:

OPPORTUNITIES:
-

RISKS:
-

SENTIMENT:
-
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a financial analyst."},
                {"role": "user", "content": prompt}
            ],
        },
        timeout=30
    )

    data = response.json()


    # 🔥 IMPORTANT FIX
    if "error" in data:
        return f"API Error: {data['error']}"

    return data["choices"][0]["message"]["content"]



    # 🔥 IMPORTANT FIX
    if "error" in data:
        return f"API Error: {data['error']}"

    return data["choices"][0]["message"]["content"]
