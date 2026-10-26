"""Processing fee calculation."""

from card_fees.pricing import CARD_RATES
from card_fees.validation import validate_transaction


def calculate_fee(amount, card_type="standard", verified=False):
    """Return the processing fee in dollars, rounded to the cent."""
    validate_transaction(amount, card_type, verified=verified)
    pricing = CARD_RATES[card_type]
    fee = amount * pricing["rate"] + pricing["fixed"]
    return round(fee, 2)
