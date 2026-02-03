#!/usr/bin/env python3
import requests
import datetime

# List of backend URLs to ping
URLS = [
                # Replace with actual project 1
       # Replace with actual project 2
    "https://watchflow-backend.onrender.com" ,
    "https://smartsession-backend-0czk.onrender.com" ,# Replace with actual project 3
    "https://fluentedge-backend.onrender.com"
    
    
]

def ping_backend(url):
    try:
        print(f"{datetime.datetime.now()}: Pinging {url}")
        response = requests.get(url, timeout=30)
        print(f"Response: {response.status_code}")

        if response.status_code == 200:
            print("✅ Backend is alive")
        else:
            print(f"⚠️ Unexpected status code: {response.status_code}")

    except Exception as e:
        print(f"❌ Error pinging {url}: {e}")

if __name__ == "__main__":
    for url in URLS:
        ping_backend(url)
