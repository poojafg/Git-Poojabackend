from unittest.mock import Mock

import pytest

from order_service import place_order


def test_place_order_returns_completed_order_and_notifies_once(sample_cart):
    # Arrange
    notifier = Mock()

    # Act
    result = place_order(sample_cart, "student", "pickup", notifier)

    # Assert
    assert result == {
        "subtotal": 10.00,
        "discount": 1.00,
        "delivery_fee": 0.00,
        "total": 9.00,
    }
    notifier.send.assert_called_once_with(result)


def test_place_order_passes_completed_order_to_notifier(sample_cart):
    # Arrange
    notifier = Mock()

    # Act
    result = place_order(sample_cart, "regular", "delivery", notifier)

    # Assert
    assert notifier.send.call_args.args[0] == result


def test_place_order_does_not_notify_when_order_is_invalid():
    # Arrange
    notifier = Mock()
    invalid_cart = [{"item": "coffee", "quantity": 0}]

    # Act / Assert
    with pytest.raises(ValueError):
        place_order(invalid_cart, "regular", "pickup", notifier)

    notifier.send.assert_not_called()
