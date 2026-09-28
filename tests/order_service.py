from checkout import calculate_order


def place_order(cart, customer_type, order_type, notifier):
    """
    Calculate an order, send a notification,
    and return the completed order.

    If calculate_order raises an exception,
    the notifier will never be called.
    """

    order = calculate_order(
        cart,
        customer_type,
        order_type,
    )

    notifier.send(order)

    return order