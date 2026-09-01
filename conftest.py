import os
from dotenv import load_dotenv
import pytest
import requests
from uuid import uuid4

load_dotenv()

@pytest.fixture(scope='session')
def base_url():
    url = os.getenv("STATUSWATCH_BASE_URL", "").strip()
    if not url:
        pytest.fail("STATUSWATCH_BASE_URL doesn't exist, check STATUSWATCH_BASE_URL in env")
    return url.rstrip("/")

@pytest.fixture(scope='session')
def admin_token(base_url):
    admin_username = os.getenv("ADMIN_USERNAME", "").strip()
    if not admin_username:
        pytest.fail("ADMIN_USERNAME doesn't exist, check in ENV")
    
    admin_password = os.getenv("ADMIN_PASSWORD", "").strip()
    if not admin_password:
        pytest.fail("ADMIN_PASSWORD doesn't exist, check in ENV")
    auth_url = base_url + "/api/auth/login"
    payload = {"username": admin_username, "password": admin_password}
    response = requests.post(auth_url, json=payload, timeout=10)
    if response.status_code != 200:
        pytest.fail(f"{response.url} returned {response.status_code}, text: {response.text[:300]}")
    return response.json()["token"]

@pytest.fixture(scope="function")
def auth_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}"}

@pytest.fixture(scope="function")
def temp_service(auth_headers,base_url):
    name = str(uuid4())

    service_post_url = base_url + "/api/services"
    payload = {"name": "qa-test-" + name, "url": service_post_url, "interval_seconds": 30}
    response = requests.post(service_post_url, json=payload, headers=auth_headers, timeout=10)
    if response.status_code != 201:
        pytest.fail(f"{response.url} returned {response.status_code}, text: {response.text[:300]}")
    service = response.json()["service"]
    service_id = service["id"]
    yield service
    
    delete_response = requests.delete(f"{service_post_url}/{service_id}", headers=auth_headers, timeout=10)
    if delete_response.status_code not in {200,204,404}:
        raise RuntimeError(f"Can't delete service: {delete_response.status_code} {delete_response.text[:200]}")