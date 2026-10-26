"""Card pricing table.

Each card type has a percentage rate applied to the transaction amount
plus a fixed per-transaction fee in dollars.
"""

CARD_RATES = {
    "standard": {"rate": 0.029, "fixed": 0.30},
    "premium": {"rate": 0.035, "fixed": 0.30},
    "business": {"rate": 0.025, "fixed": 0.25},
}
