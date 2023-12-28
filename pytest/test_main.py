import pytest
import core, helper
from core import app

def test_book():
    # Define inputs and expected output
    title = "Test Title"
    author = "Test Author"
    action = "Test Action"
    results = 1

    # Assert that the inputs are not empty and are of the correct type
    assert title != ""
    assert author != ""
    assert isinstance(action, str), "Action is not a string"
    assert isinstance(results, int) and 1 <= results <= 40, "Results is not an integer between 1 and 40"

def title():
    title = "Test Title"
    results = 1

    assert title != ""
    assert isinstance(results, int) and 1 <= results <= 40, "Results is not an integer between 1 and 40"

def author():
    author = "Test Author"
    results = 1

    assert author != ""
    assert isinstance(results, int) and 1 <= results <= 40, "Results is not an integer between 1 and 40"
