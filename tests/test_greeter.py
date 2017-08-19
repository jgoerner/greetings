import pytest

from greetings import greeter
NAME = "Joshua"


def test_greeting_not_supported_language():
    with pytest.raises(ValueError):
        greeter.greet("Joshua", "ES")


def test_greet_german():
    assert greeter.greet(NAME, "DE") == "Hallo Joshua, Wie geht es dir"


def test_greet_english():
    assert greeter.greet(NAME, "EN") == "Hello Joshua, How are you"


def test_greet_chinese():
    assert greeter.greet(NAME, "ZH") == "Ni hao Joshua, Ni hao ma"
