import pytest
import requests

@pytest.mark.smoke
def test_health_check(base_url):
    response = requests.get(f"{base_url}/api/health", timeout=5)
    assert response.status_code == 200