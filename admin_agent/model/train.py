from admin_agent.model import model
import numpy as np

X = np.array([
    [10, 2048, 100, 10],
    [15, 3072, 120, 15],
    [9, 1024, 90, 5],
    [14, 4096, 110, 12],
    [13, 2560, 105, 14],
])

model.train_model(X)
print("Anomaly detection model trained and saved to model.pkl")