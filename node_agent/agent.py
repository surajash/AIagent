import requests
import random
import time

def collect_metrics():
    # Simulated data: [CPU, Memory, Disk] usage in %
    return [random.randint(40, 95) for _ in range(3)]

def send_alert(metrics):
    data = {"metrics": metrics}
    response = requests.post("http://localhost:8000/alert", json=data)
    print("Server response:", response.json())

if __name__ == "__main__":
    while True:
        metrics = collect_metrics()
        print("Collected metrics:", metrics)
        send_alert(metrics)
        time.sleep(10)
