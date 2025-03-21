import pytest
import json
from shared_utils import attempt_login

with open("../resources/credentials_test_data.json", "r") as file:
    TEST_DATA = json.load(file)

@pytest.mark.parametrize("payload", TEST_DATA["sql_injections"])
def test_sql_injection(payload):
    """Test authentication bypass attempts."""
    response = attempt_login(payload["email"], payload["password"])
    assert response is not None, "Request failed."
    assert response.status_code == 200, f"SQL Injection Failed: {payload['email']}"

@pytest.mark.parametrize("creds", TEST_DATA["common_creds"])
def test_common_credentials(creds):
    """Test authentication using easy to guess admin credentials."""
    response = attempt_login(creds["email"], creds["password"])
    assert response is not None, "Request failed."
    assert response.status_code == 200, f"Common credentials failed for {creds['email']}"

def test_no_password_login():
    """Test if login works without password."""
    payload = TEST_DATA["no_password"]
    response = attempt_login(payload["email"], payload["password"])
    assert response is not None, "Request failed."
    assert response.status_code != 200, "Empty password login should not be allowed!"
