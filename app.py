from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from openai_helper import classify_ticket

app = FastAPI(title="Smart Support Ticket Classifier")


class TicketList(BaseModel):
    messages: List[str]


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/classify")
def classify(tickets: TicketList):
    results = []

    for msg in tickets.messages:
        result = classify_ticket(msg)

        results.append({
            "message": msg,
            "category": result.get("category"),
            "priority": result.get("priority")
        })

    return results