import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import add_numbers, is_valid_port

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_is_valid_port():
    assert is_valid_port(80) is True
    assert is_valid_port(70000) is False
