# Smart Support Ticket Classifier (Ollama) 

## Ollama was used as a local alternative due to API quota limitations, with the system designed to be easily adaptable to OpenAI
## Ensure Ollama is installed and running locally before starting the server.
## Overview

An AI-powered system that classifies customer support tickets into categories and assigns priority levels.
This version uses a local LLM (Ollama) for cost-free and combines LLM output with rule-based logic for improved consistency.

## Features

* Classifies tickets into categories such as Billing, Technical, Account, General, Complaint, and Feature Request
* Assigns priority levels (Low, Medium, High)
* Provides a confidence score
* REST API built using FastAPI
* Stores ticket logs with timestamp and unique ID

## Tech Stack

* Python
* FastAPI
* Ollama (Local LLM)
* JSON (for storage)

## How It Works

1. User sends a support message
2. The LLM classifies category and priority
3. Rule-based logic ensures consistent output
4. Result is returned via API
5. Ticket is stored with metadata for tracking

## API Endpoints
### POST /classify

Request:

```json
{
  "message": "My payment failed but money was deducted"
}
```

Response:

```json
{
  "ticket_id": "...",
  "timestamp": "...",
  "category": "Billing",
  "priority": "High",
  "confidence": 95
}
```

### GET /logs
Returns all stored ticket logs
## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Conclusion
Used Ollama. It can be extended to use OpenAI API for improved accuracy and performance.
