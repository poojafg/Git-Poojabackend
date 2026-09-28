import pytest

from checkout import (
    calculate_delivery_fee,
    calculate_discount,
    calculate_order,
    calculate_subtotal,
)


def test_calculate_subtotal_for_valid_cart(sample_cart):
    # Arrange / Act
    result = calculate_subtotal(sample_cart)

    # Assert
    assert result == 10.00


def test_calculate_subtotal_for_different_products_and_quantities():
    # Arrange
    cart = [
        {"item": "tea", "quantity": 2},
        {"item": "sandwich", "quantity": 1},
        {"item": "salad", "quantity": 1},
    ]

    # Act
    result = calculate_subtotal(cart)

    # Assert
    assert result == 16.50


def test_calculate_subtotal_rejects_empty_cart():
    with pytest.raises(ValueError):
        calculate_subtotal([])


def test_calculate_subtotal_rejects_unknown_menu_item():
    cart = [{"item": "pizza", "quantity": 1}]

    with pytest.raises(ValueError):
        calculate_subtotal(cart)


def test_calculate_subtotal_rejects_zero_quantity():
    cart = [{"item": "coffee", "quantity": 0}]

    with pytest.raises(ValueError):
        calculate_subtotal(cart)


def test_calculate_subtotal_rejects_negative_quantity():
    cart = [{"item": "coffee", "quantity": -1}]

    with pytest.raises(ValueError):
        calculate_subtotal(cart)


@pytest.mark.parametrize("quantity", ["2", 2.0, True, False])
def test_calculate_subtotal_rejects_non_integer_quantity(quantity):
    cart = [{"item": "coffee", "quantity": quantity}]

    with pytest.raises(ValueError):
        calculate_subtotal(cart)


def test_regular_customer_receives_no_discount():
    assert calculate_discount(20.00, "regular") == 0.00


def test_student_receives_no_discount_below_ten_euros():
    assert calculate_discount(9.99, "student") == 0.00


def test_student_receives_ten_percent_discount_at_exactly_ten_euros():
    assert calculate_discount(10.00, "student") == 1.00


def test_student_receives_ten_percent_discount_above_ten_euros():
    assert calculate_discount(20.00, "student") == 2.00


def test_staff_customer_receives_fifteen_percent_discount():
    assert calculate_discount(20.00, "staff") == 3.00


def test_unknown_customer_type_is_rejected():
    with pytest.raises(ValueError):
        calculate_discount(20.00, "vip")


def test_pickup_has_no_delivery_fee():
    assert calculate_delivery_fee(15.00, "pickup") == 0.00


def test_delivery_below_twenty_euros_costs_four_euros():
    assert calculate_delivery_fee(19.99, "delivery") == 4.00


def test_delivery_at_exactly_twenty_euros_is_free():
    assert calculate_delivery_fee(20.00, "delivery") == 0.00


def test_delivery_above_twenty_euros_is_free():
    assert calculate_delivery_fee(25.00, "delivery") == 0.00


def test_unknown_order_type_is_rejected():
    with pytest.raises(ValueError):
        calculate_delivery_fee(20.00, "courier")


def test_calculate_order_combines_subtotal_discount_delivery_and_total():
    # Arrange: subtotal = 20.00, student discount = 2.00, delivery = 0.00
    cart = [
        {"item": "sandwich", "quantity": 2},
        {"item": "salad", "quantity": 1},
        {"item": "coffee", "quantity": 1},
    ]

    # Act
    result = calculate_order(cart, "student", "delivery")

    # Assert
    assert result == {
        "subtotal": 20.00,
        "discount": 2.00,
        "delivery_fee": 0.00,
        "total": 18.00,
    }


def test_calculate_order_propagates_invalid_cart_error():
    with pytest.raises(ValueError):
        calculate_order([], "regular", "pickup")
