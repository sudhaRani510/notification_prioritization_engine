from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random
from datetime import datetime

app = FastAPI(title="AI Notification Prioritization Engine")

# Temporary in-memory storage
notifications = []

class NotificationRequest(BaseModel):
    customer_id: str
    event_type: str

class NotificationResponse(BaseModel):
    notification_id: int
    customer_id: str
    event_type: str
    priority: str
    created_at: datetime

# Simulated ML scoring function
def calculate_priority():
    ml_score = random.random()  # simulate ML output (0–1)

    if ml_score >= 0.75:
        return "High"
    elif ml_score >= 0.4:
        return "Medium"
    else:
        return "Low"

@app.post("/notifications", response_model=NotificationResponse)
def create_notification(request: NotificationRequest):
    priority = calculate_priority()

    notification = {
        "notification_id": len(notifications) + 1,
        "customer_id": request.customer_id,
        "event_type": request.event_type,
        "priority": priority,
        "created_at": datetime.now()
    }

    notifications.append(notification)
    return notification

@app.get("/notifications", response_model=List[NotificationResponse])
def get_notifications():
    return notifications

@app.get("/health")
def health_check():
    return {"status": "Notification Engine Running Successfully"}
