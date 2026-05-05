import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_ticket(message: str):
    prompt = f"""
Classify this support ticket into:
- Category (Billing, Technical, Account, General)
- Priority (Low, Medium, High)

Ticket: "{message}"

Respond ONLY in JSON:
{{
  "category": "...",
  "priority": "..."
}}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a strict classifier."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        return {"error": str(e)}