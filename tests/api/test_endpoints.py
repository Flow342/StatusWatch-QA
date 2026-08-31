import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.smoke
def test_health_check():
    url = os.getenv("URL")
    response = requests.get(f"{url}/api/health", timeout=5)
    assert response.status_code == 200