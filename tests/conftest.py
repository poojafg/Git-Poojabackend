import pytest


@pytest.fixture
def sample_cart():
    return [
        {"item": "coffee", "quantity": 2},
        {"item": "cake", "quantity": 1},
    ]
