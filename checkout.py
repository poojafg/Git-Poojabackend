MENU = {
    "coffee": 3.00,
    "tea": 2.50,
    "sandwich": 5.50,
    "salad": 6.00,
    "cake": 4.00,
}


def calculate_subtotal(cart):
    """
    Calculate the subtotal of all items in the cart.

    Raises:
        ValueError:
            - if the cart is empty
            - if an item does not exist on the menu
            - if quantity is not an integer
            - if quantity is zero or negative
    """

    if not cart:
        raise ValueError("Cart cannot be empty")

    subtotal = 0

    for cart_item in cart:
        item_name = cart_item["item"]
        quantity = cart_item["quantity"]

        if item_name not in MENU:
            raise ValueError(f"Unknown menu item: {item_name}")

        # bool is technically a subclass of int in Python,
        # but True/False should not be accepted as quantities.
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Quantity must be an integer")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        subtotal += MENU[item_name] * quantity

    return round(subtotal, 2)


def calculate_discount(subtotal, customer_type):
    """
    Calculate the discount amount.

    Rules:
        regular -> 0%
        student -> 10% when subtotal >= 10
        staff   -> 15%

    Raises:
        ValueError if customer_type is unknown.
    """

    if customer_type == "regular":
        discount = 0

    elif customer_type == "student":
        if subtotal >= 10:
            discount = subtotal * 0.10
        else:
            discount = 0

    elif customer_type == "staff":
        discount = subtotal * 0.15

    else:
        raise ValueError(f"Unknown customer type: {customer_type}")

    return round(discount, 2)


def calculate_delivery_fee(subtotal, order_type):
    """
    Calculate the delivery fee.

    Rules:
        pickup -> free
        delivery:
            subtotal < 20  -> 4 euro
            subtotal >= 20 -> free

    Raises:
        ValueError if order_type is unknown.
    """

    if order_type == "pickup":
        return 0.00

    if order_type == "delivery":
        if subtotal < 20:
            return 4.00

        return 0.00

    raise ValueError(f"Unknown order type: {order_type}")


def calculate_order(cart, customer_type, order_type):
    """
    Calculate a complete order summary.
    """

    subtotal = calculate_subtotal(cart)

    discount = calculate_discount(
        subtotal,
        customer_type,
    )

    delivery_fee = calculate_delivery_fee(
        subtotal,
        order_type,
    )

    total = subtotal - discount + delivery_fee

    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "delivery_fee": round(delivery_fee, 2),
        "total": round(total, 2),
    }