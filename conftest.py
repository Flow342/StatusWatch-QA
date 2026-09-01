import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.fixture(scope='session')
def base_url():
    url = os.getenv("URL")
    if not url:
        pytest.fail("URL doesn't exist, check .env")
    return url