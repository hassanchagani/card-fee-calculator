import pytest

from card_fees import ValidationError, calculate_fee


def test_rejects_unknown_card_type():
    with pytest.raises(ValidationError):
        calculate_fee(50.00, "platinum")


def test_rejects_zero_amount():
    with pytest.raises(ValidationError):
        calculate_fee(0, "standard")


def test_rejects_negative_amount():
    with pytest.raises(ValidationError):
        calculate_fee(-10.00, "standard")


def test_rejects_amount_over_limit():
    with pytest.raises(ValidationError):
        calculate_fee(60000.00, "standard", verified=True)


def test_large_transaction_requires_verification():
    with pytest.raises(ValidationError):
        calculate_fee(15000.00, "standard")
