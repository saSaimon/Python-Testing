import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("I will be execute in fixtureDemo method.")

    def test_fixtureDemo1(self):
        print("I will be execute in fixtureDemo1 method.")

    def test_fixtureDemo2(self):
        print("I will be execute in fixtureDemo2 method.")

    def test_fixtureDemo3(self):
        print("I will be execute in fixtureDemo3 method.")
