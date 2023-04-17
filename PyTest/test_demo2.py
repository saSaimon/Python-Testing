# Any pytest file start with test_
# pytest method always will start with test
# Any code should wrapped in method only
# Method name should have sense
# -k stans for method name execution.-s logs output  -v stands for more info metadata
# you can run specific file with py.test <file.name>
# to mark any testcase type @pytest.mark.<name> and to run it into console py.test -m <name> -s -v
# you can skip test with @pytest.mark.skip
# if you dont want to skip any test case but not want to show on the output then you should use @pytest.test.xfail
# fixture are used as setup tear down method for test cases conftest file to generalize fixture and
# make it available to all the tesst cases.
# datadriven and parameterization can be done with return statements in tuple format
# when you  define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "hello"
    assert msg == "hi", "Test failed because string do not match."


def test_secondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match."


@pytest.fixture()
def setup():
    print("I will be execute first.")


def test_fixtureDemo(setup):
    print("I will be execute in fixtureDemo method.")

