from card_fees import calculate_fee


def test_standard_fee():
    assert calculate_fee(100.00, "standard") == 3.00


def test_premium_fee():
    assert calculate_fee(200.00, "premium") == 7.30


def test_business_fee():
    assert calculate_fee(1000.00, "business") == 25.25


def test_default_card_type_is_standard():
    assert calculate_fee(100.00) == calculate_fee(100.00, "standard")


def test_verified_large_transaction():
    assert calculate_fee(20000.00, "business", verified=True) == 500.25
