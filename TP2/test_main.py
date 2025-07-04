from main import hello
import pytest
import time


def test_hello():
    assert hello() == "Hello, John Doe!"


def test_hello_custom_name():
    assert hello("EPSI") == "Hello, EPSI Doe!"


def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)


def test_hello_performance():
    start = time.time()
    for _ in range(1000):
        hello("EPSI")
    duration = time.time() - start
    assert duration < 1


def test_hello_full_name():
    assert hello("Jane", "Smith") == "Hello, Jane Smith!"
