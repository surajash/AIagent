import requests
import time
from metrics_collector import collect_metrics

ADMIN_API_URL = "http://localhost:8000/alert"

def send_metrics():
    metrics = collect_metrics()
    payload = {"metrics": metrics}
    print("Sending metrics to Admin Agent:", payload)
    try:
        response = requests.post(ADMIN_API_URL, json=payload)
        if response.ok:
            print("Admin Response:", response.json())
        else:
            print(f"Failed! Status Code: {response.status_code}")
    except Exception as e:
        print("Error sending data to Admin Agent:", str(e))

if __name__ == "__main__":
    print("Node Agent started. Sending metrics every 10 seconds...")
    while True:
        send_metrics()
        time.sleep(10)
