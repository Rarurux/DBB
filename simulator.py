# simulator.py
import requests
import time
import random
from datetime import datetime

URL = "http://127.0.0.1:8000/api/ingest"

print("🚀 Simulator running... Sending stream to backend.")

while True:
    # 80% chance of normal data, 20% chance of triggering an incident
    is_spike = random.random() < 0.2
    
    data = {
        "device_or_user_id": "Server_Alpha_01",
        "cpu_usage": round(random.uniform(88.0, 99.0) if is_spike else random.uniform(20.0, 50.0), 2),
        "ram_usage": round(random.uniform(86.0, 98.0) if is_spike else random.uniform(30.0, 60.0), 2),
        "amount": round(random.uniform(9500.0, 15000.0) if is_spike else random.uniform(10.0, 200.0), 2),
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    
    try:
        res = requests.post(URL, json=data)
        print(f"Sent payload | Anomaly Flagged: {res.json().get('anomaly_detected')}")
    except Exception as e:
        print(f"Backend not reachable: {e}")
        
    time.sleep(2) # Send data every 2 seconds