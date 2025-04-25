from sklearn.ensemble import IsolationForest
import joblib
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def train_model(X):
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)
    joblib.dump(model, MODEL_PATH)

def load_model():
    return joblib.load(MODEL_PATH)

def analyze_anomaly(model, features: list):
    return model.predict([features])[0] == -1