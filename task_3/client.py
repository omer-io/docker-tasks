import requests
import time

url = 'http://server:5000'
def health_check():
    response = requests.get('http://server:5000/health')
    if response.status_code == 200:
        print("Health check passed")
    else:
        print("Health check failed")

def send_ping():
    response = requests.post('http://server:5000/ping', json={"type": "ping"})
    if response.status_code == 200:
        print("Ping response:", response.json())
    else:
        print("Ping request failed")

def send_data():
    response = requests.post('http://server:5000/data', json={"jsonrpc": "2.0", "method": "message-1"})
    if response.status_code == 200:
        print("Data response:", response.json())
    else:
        print("Data request failed")

while True:
    health_check()
    send_ping()
    send_data()
    time.sleep(5)
