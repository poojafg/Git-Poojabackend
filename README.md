# ReDI Café Checkout

A small Python café checkout application with a pytest test suite.

## Project structure

```text
redi-A26-Lesson5/
├── main.py
├── checkout.py
├── order_service.py
├── notifier.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── tests/
    ├── conftest.py
    ├── test_checkout.py
    └── test_order_service.py
```

## Business rules

### Menu

| Item | Price |
|---|---:|
| Coffee | €3.00 |
| Tea | €2.50 |
| Sandwich | €5.50 |
| Salad | €6.00 |
| Cake | €4.00 |

### Subtotal

The subtotal is the sum of each menu item's price multiplied by its quantity.

Invalid carts raise `ValueError` when:
- the cart is empty;
- an item is not on the menu;
- quantity is zero;
- quantity is negative;
- quantity is not an integer.

### Discounts

- `regular`: 0%
- `student`: 10% when subtotal is at least €10
- `staff`: 15%

Unknown customer types raise `ValueError`.

### Delivery

- `pickup`: €0.00
- `delivery` below €20: €4.00
- `delivery` at or above €20: €0.00

Unknown order types raise `ValueError`.

### Complete orders

The final total is:

```text
total = subtotal - discount + delivery_fee
```

### Order service

`place_order()` calculates the completed order, sends it to the notifier, and returns it. If order calculation fails, the notifier is not called.

## Setup with pip

Create and activate a virtual environment:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Setup with uv

Alternatively:

```bash
uv sync
```

You do not need to use both workflows.

## Run the café

```bash
python main.py
```

Or with uv:

```bash
uv run python main.py
```

## Run tests

```bash
pytest -v
```

Or:

```bash
uv run pytest -v
```

## Run checkout tests only

```bash
pytest tests/test_checkout.py -v
```

## Run order-service tests only

```bash
pytest tests/test_order_service.py -v
```

## Test coverage

```bash
pytest --cov=. --cov-report=term-missing
```

Or:

```bash
uv run pytest --cov=. --cov-report=term-missing
```

The test suite includes:
- valid checkout calculations;
- invalid input validation;
- discount rules and the €10 boundary;
- delivery rules and the €20 boundary;
- complete order calculations;
- pytest fixtures;
- mocked notifier interactions;
- successful and invalid order-service behaviour.
