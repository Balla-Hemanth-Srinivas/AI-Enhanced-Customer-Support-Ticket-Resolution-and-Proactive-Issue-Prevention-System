from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import uvicorn

# Initialize FastAPI application
app = FastAPI()

# Define models for input data
class EmailPayload(BaseModel):
    sender: str
    subject: str
    content: str

class PriorityCheck(BaseModel):
    level: str
    description: str

class UserQuery(BaseModel):
    query: str

# Function to perform sentiment analysis
def analyze_sentiment(message: str) -> str:
    # Basic placeholder for sentiment analysis logic
    if "good" in message.lower() or "great" in message.lower():
        return "positive"
    elif "bad" in message.lower() or "poor" in message.lower():
        return "negative"
    else:
        return "neutral"

# Endpoint to analyze sentiment
@app.get("/sentiment")
async def sentiment_analysis(text: str):
    sentiment = analyze_sentiment(text)
    return {"input_text": text, "sentiment": sentiment}

# Endpoint to handle incoming email webhook
@app.post("/email-webhook")
async def email_webhook(payload: EmailPayload):
    print(f"Received email from: {payload.sender} | Subject: {payload.subject}")
    # Logic to process the email can be added here
    return {"status": "success", "message": "Email processed successfully"}

# Endpoint to check if an issue needs escalation
@app.post("/priority-check")
async def priority_check(data: PriorityCheck):
    needs_escalation = data.level.lower() == "high"
    return {
        "requires_escalation": needs_escalation,
        "issue_details": data.description
    }

# Endpoint to generate automated response for user queries
@app.post("/auto-response")
async def auto_response(user_query: UserQuery):
    automated_reply = f"Thank you for your question: '{user_query.query}'. Our team will get back to you shortly."
    return {"reply": automated_reply}

# Main application entry point
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)