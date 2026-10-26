"""Transaction validation rules."""

from card_fees.pricing import CARD_RATES

MAX_TRANSACTION = 50_000
VERIFICATION_THRESHOLD = 10_000


class ValidationError(ValueError):
    """Raised when a transaction fails validation."""


def validate_transaction(amount, card_type, verified=False):
    """Validate a transaction before a fee is calculated.

    Transactions above VERIFICATION_THRESHOLD require the cardholder's
    identity to be verified. This is a fraud control and must not be
    bypassed.
    """
    if card_type not in CARD_RATES:
        raise ValidationError(f"Unknown card type: {card_type}")
    if amount <= 0:
        raise ValidationError("Amount must be greater than zero")
    if amount > MAX_TRANSACTION:
        raise ValidationError(f"Amount exceeds the ${MAX_TRANSACTION:,} limit")
    if amount > VERIFICATION_THRESHOLD and not verified:
        raise ValidationError(
            f"Transactions over ${VERIFICATION_THRESHOLD:,} require identity verification"
        )
