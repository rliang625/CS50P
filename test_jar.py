from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._size == 0

def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar._size == 1
    with pytest.raises(ValueError):
        jar.deposit(15)

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3
    jar.withdraw(2)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(100)
