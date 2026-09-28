from checkout import MENU
from notifier import OrderNotifier
from order_service import place_order


def display_menu():
    print("\n=== ReDI Café Menu ===")
    for item, price in MENU.items():
        print(f"{item.title():<12} €{price:.2f}")
    print()


def build_cart():
    cart = []

    print("Add items to your order.")
    print("Type 'done' when you are finished.\n")

    while True:
        item = input("Item: ").strip().lower()

        if item == "done":
            break

        if item not in MENU:
            print("That item is not on the menu. Please try again.\n")
            continue

        quantity_text = input("Quantity: ").strip()

        try:
            quantity = int(quantity_text)
        except ValueError:
            print("Quantity must be a whole number.\n")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

        cart.append(
            {
                "item": item,
                "quantity": quantity,
            }
        )

        print(f"Added {quantity} × {item}.\n")

    return cart


def choose_customer_type():
    valid_customer_types = {
        "regular",
        "student",
        "staff",
    }

    while True:
        print("\nCustomer types: regular, student, staff")
        customer_type = input("Customer type: ").strip().lower()

        if customer_type in valid_customer_types:
            return customer_type

        print("Unknown customer type. Please try again.")


def choose_order_type():
    valid_order_types = {
        "pickup",
        "delivery",
    }

    while True:
        print("\nOrder types: pickup, delivery")
        order_type = input("Order type: ").strip().lower()

        if order_type in valid_order_types:
            return order_type

        print("Unknown order type. Please try again.")


def display_order_summary(order):
    print("\n=== Order Summary ===")
    print(f"Subtotal:      €{order['subtotal']:.2f}")
    print(f"Discount:     -€{order['discount']:.2f}")
    print(f"Delivery fee:  €{order['delivery_fee']:.2f}")
    print("------------------------")
    print(f"Total:         €{order['total']:.2f}")


def main():
    print("Welcome to the ReDI Café Checkout!")

    display_menu()
    cart = build_cart()

    if not cart:
        print("\nNo items were added. Goodbye!")
        return

    customer_type = choose_customer_type()
    order_type = choose_order_type()

    notifier = OrderNotifier()

    try:
        order = place_order(
            cart,
            customer_type,
            order_type,
            notifier,
        )
    except ValueError as error:
        print(f"\nCould not place order: {error}")
        return

    display_order_summary(order)
    print("\nOrder placed successfully!")


if __name__ == "__main__":
    main()
