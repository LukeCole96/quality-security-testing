import pytest
import json
from shared_utils import attempt_login

with open("../resources/credentials_test_data.json", "r") as file:
    TEST_DATA = json.load(file)

@pytest.mark.parametrize("weak_password", TEST_DATA["weak_passwords"])
def test_weak_password_policy(weak_password):
    payload = {"email": "newuser@juice-sh.op", "password": weak_password}
    response = attempt_login(payload["email"], payload["password"])
    assert response.status_code != 200, f"Weak password '{weak_password}' was accepted!"

def test_brute_force_protection():
    email = TEST_DATA["valid_user"]["email"]
    
    for i in range(10):
        response = attempt_login(email, f"wrongpassword{i}")
        print(f"Attempt {i+1}: {response.status_code}")
    
    assert response.status_code == 429 or response.status_code == 403, "No brute-force protection detected."