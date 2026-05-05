from fastapi import FastAPI
from pydantic import BaseModel
from openai_helper import classify_ticket
import json
import os
from datetime import datetime
import uuid

app = FastAPI(title="Smart Support Ticket Classifier")

LOG_FILE = "tickets_log.json"


class Ticket(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "API is running"}


def save_ticket(data):
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


@app.post("/classify")
def classify(ticket: Ticket):
    result = classify_ticket(ticket.message)

    log_data = {
        "ticket_id": str(uuid.uuid4()),   # 🔥 unique ID
        "timestamp": datetime.now().isoformat(),  # 🔥 time
        "message": ticket.message,
        "category": result.get("category"),
        "priority": result.get("priority"),
        "confidence": result.get("confidence")
    }

    save_ticket(log_data)

    return log_data


@app.get("/logs")
def get_logs():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:
        return json.load(f)