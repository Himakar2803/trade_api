# Trade Sector Analysis API 🚀

A FastAPI-based backend service that analyzes market sectors using AI
and returns structured insights including Opportunities, Risks, and Sentiment.

This project was built as part of an AI Engineer assignment.

---

## 🔧 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- OpenRouter AI (LLM integration)
- dotenv
- REST API

---

## 📁 Project Structure

trade_api/
│
├── main.py          # FastAPI app & API routes
├── ai_engine.py     # AI integration logic (LLM calls)
├── auth.py          # API key validation
├── data_fetch.py   # Market data simulation
├── rate_limit.py   # Rate limiting logic
├── requirements.txt
├── .env             # Environment variables (NOT committed)
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Himakar2803/trade_api.git
cd trade_api
