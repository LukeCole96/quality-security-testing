import requests
import datetime
import json

BASE_URL = "http://localhost:3000"
LOGIN_URL = f"{BASE_URL}/rest/user/login"

def attempt_login(email, password, headers=None):
    try:
        response = requests.post(LOGIN_URL, json={"email": email, "password": password}, headers=headers)
        log_request_response(email, password, response)
        return response
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Unable to connect to {LOGIN_URL}. Exception: {e}")
        return None

def extract_token(response):
    try:
        token = response.json().get("authentication", {}).get("token")
        if token:
            print(f"\nExtracted JWT Token: {token}")
        else:
            print("\nNo JWT Token found in response.")
        return token
    except Exception as e:
        print(f"Error extracting token: {e}")
        return None

def log_request_response(email, password, response):
    print("\n========================================")
    print(f"TEST: Attempting login")
    print(f"Timestamp: {datetime.datetime.now().isoformat()}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print("\n--- HTTP Request ---")
    print(f"POST {LOGIN_URL}")
    print("Headers: {'Content-Type': 'application/json'}")
    print(f"Payload: {json.dumps({'email': email, 'password': password}, indent=4)}")

    print("\n--- HTTP Response ---")
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Body: {response.text}")

    print("========================================\n")
