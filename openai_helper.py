import requests
import json

def classify_ticket(message: str):
    prompt = f"""
You are a STRICT customer support classifier.

Rules:
- Categories: Billing, Technical, Account, General, Complaint, Feature Request
- Priorities: Low, Medium, High
- If money/payment/refund/deducted → ALWAYS Billing + High
- Provide a confidence score (0 to 100)

Ticket: "{message}"

Respond ONLY in VALID JSON:
{{
  "category": "...",
  "priority": "...",
  "confidence": 90
}}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:latest",
            "prompt": prompt,
            "stream": False,
            "temperature": 0
        }
    )

    data = response.json()

    if "response" not in data:
        return {"error": "Invalid response", "raw": data}

    result = data["response"]

    try:
        parsed = json.loads(result)
    except:
        return {"error": "Invalid JSON", "raw_output": result}

    # Rule-based correction
    if any(word in message.lower() for word in ["payment", "refund", "money", "deducted"]):
        parsed["category"] = "Billing"
        parsed["priority"] = "High"
        parsed["confidence"] = 95

    return parsed