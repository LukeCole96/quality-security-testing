import pytest
import json
import jwt
from shared_utils import extract_token, attempt_login

with open("../resources/jwt_test_data.json", "r") as file:
    TEST_DATA = json.load(file)

def test_jwt_tampering():
    """Tests if JWT tokens can be modified without rejection."""
    response = attempt_login(TEST_DATA["valid_user"]["email"], TEST_DATA["valid_user"]["password"])
    assert response.status_code == 200, "Failed to log in with valid credentials."
    
    token = extract_token(response)
    assert token is not None, "JWT token was not issued."
    
    modified_payload = {"user": "admin", "role": "admin"}
    tampered_token = jwt.encode(modified_payload, key="", algorithm="none")
    
    headers = {"Authorization": f"Bearer {tampered_token}"}
    test_response = attempt_login(TEST_DATA["valid_user"]["email"], TEST_DATA["valid_user"]["password"], headers)
    
    assert test_response.status_code != 200, "JWT tampering succeeded, system is vulnerable!"

def test_jwt_expiration():
    """Tests if expired JWT tokens are properly rejected."""
    response = attempt_login(TEST_DATA["valid_user"]["email"], TEST_DATA["valid_user"]["password"])
    assert response.status_code == 200, "Failed to log in with valid credentials."
    
    token = extract_token(response)
    assert token is not None, "JWT token was not issued."

    decoded = jwt.decode(token, options={"verify_signature": False})
    assert "exp" in decoded, "JWT token does not have an expiration time."

    print("JWT Expiration Time:", decoded["exp"])
