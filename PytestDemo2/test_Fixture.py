import pytest


@pytest.mark.usefixtures
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute step in fixture demo method")

    def test_fixtureDemo1(self):
        print("I will execute step in fixture demo method")

    def test_fixtureDemo2(self):
        print("I will execute step in fixture demo method")

    def test_fixtureDemo2(self):
        print("I will execute step in fixture demo method")