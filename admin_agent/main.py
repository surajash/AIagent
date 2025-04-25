from fastapi import FastAPI
from admin_agent.schemas import AlertRequest
from admin_agent.model.model import load_model, analyze_anomaly
from admin_agent.utils import generate_suggestions
import uvicorn

app = FastAPI()
model = load_model()

@app.post("/alert")
async def receive_alert(alert: AlertRequest):
    features = alert.metrics
    is_anomaly = analyze_anomaly(model, features)
    if is_anomaly:
        suggestions = generate_suggestions(features)
        return {"anomaly": True, "suggestions": suggestions}
    return {"anomaly": False, "suggestions": []}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)