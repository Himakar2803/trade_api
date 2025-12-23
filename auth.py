from fastapi import HTTPException

VALID_API_KEY = "12345"

def authenticate(key: str):
    if key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
