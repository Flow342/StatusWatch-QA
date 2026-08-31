import pytest

@pytest.fixture
def generateData():
    login = "login@mail.ru"
    password = "1234"
    return {"login": login, "password": password}