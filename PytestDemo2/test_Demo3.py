import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_FirstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test fail string not match"


def test_Secondcreditcard():
    a = 4
    b = 6
    assert a+2 == 6, "addition not match"


@pytest.fixture()
def setup():
    print("I will be executing first")


def test_fixtureDemo():
    print("I will execute step in fixture demo method")

