import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("i will execute last")
