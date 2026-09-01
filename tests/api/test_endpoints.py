import pytest
import requests

@pytest.mark.smoke
def test_health_check(base_url):
    response = requests.get(f"{base_url}/api/health", timeout=5)
    assert response.status_code == 200, (
        f"GET {response.url} returned {response.status_code}, text: {response.text[:300]}"
    )

def test_temp_delete(temp_service):
    assert temp_service["id"] != 0