from numb3rs import validate


def test_basics():
    assert validate("1.2.3.4")

def test_lower_range():
    assert validate("-1.2.3.4") == False

def test_upper_range():
    assert validate("275.3.6.28") == False

def test_pass_check50():
    assert validate("1.900.1.1") == False



