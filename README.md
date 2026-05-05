# Smart Support Ticket Classifier (Ollama)

## 🚀 Overview

This project is an AI-powered system that classifies customer support tickets into categories and assigns priority levels.

This version uses a local LLM (Ollama) instead of OpenAI for cost-free execution.

---

## 🧠 Features

* Classifies tickets into categories (Billing, Technical, Account, General, etc.)
* Assigns priority (Low, Medium, High)
* Provides confidence score
* REST API using FastAPI
* Stores ticket logs with timestamp and unique ID

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Ollama (Local LLM)
* JSON storage

---

## ⚙️ How It Works

1. User sends a support message
2. LLM classifies category and priority
3. Rule-based logic improves consistency
4. Result is returned via API
5. Ticket is stored for tracking

---

## 📡 API Endpoints

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

---

### GET /logs

Returns all stored tickets

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## 💡 Note

This implementation uses Ollama. It can be extended to OpenAI API for higher accuracy.
