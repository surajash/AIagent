# AI-based Infrastructure Admin Agent

This project demonstrates a basic AI agent for infrastructure monitoring using FastAPI and ML for anomaly detection.

## Components

- **Admin Agent (FastAPI)**: Receives alerts, detects anomalies, and suggests remediations.
- **Node Agent**: Collects metrics and sends alerts.
- **ML Model**: Isolation Forest for anomaly detection.

## Run Locally

1. Train your model and save to `model.pkl`
2. Start the Admin Agent:
```bash
uvicorn admin_agent.main:app --reload --port 8000
```
3. Run the Node Agent:
```bash
python node_agent/agent.py
```

