import os
import requests
from dotenv import load_dotenv

def scan_url(target_url):
    load_dotenv()
    API_KEY = os.getenv("BP_API_KEY")
    
    if not API_KEY:
        return {"status": "error", "message": "API Key is missing from .env file."}
        
    endpoint = "https://developers.bolster.ai/api/neo/scan"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "apiKey": API_KEY,
        "urlInfo": {
            "url": target_url
        }
    }
    
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        
        if response.status_code != 200:
            return {"status": "error", "message": f"API Error: Status {response.status_code}"}
            
        data = response.json()
        
        disposition = data.get("disposition", "clean").lower()
        
        if disposition in ["phish", "scam", "malware", "suspicious"]:
            return {
                "status": "dangerous",
                "message": f"DANGER: Flagged as [{disposition.upper()}]!"
            }
        else:
            return {"status": "clean", "message": "CLEAN: The site is safe and clean"}
            
    except Exception as e:
        return {"status": "error", "message": f"Connection Failure: {str(e)}"}