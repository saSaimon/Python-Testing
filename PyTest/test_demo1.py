

import pytest


@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello")

@pytest.mark.xfail
def test_secondGReetingCreditCard():
    print("Good Morning")


def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])


# def test_crossbrowser1(crossbrowser1):
#     print(crossbrowser1[1])