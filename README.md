# card-fee-calculator

A small library for calculating card processing fees.

## Install

```
pip install cardfees
```

## Usage

```python
from cardfees import compute_fee

compute_fee(100.00, card="premium")
```

From the command line:

```
python -m cardfees --amount 100 --card premium
```

## Pricing

| Card | Rate | Fixed fee |
|------|------|-----------|
| standard | 2.7% | $0.30 |
| premium | 3.5% | $0.30 |
| business | 2.5% | $0.25 |

Fees are rounded to the nearest cent.

## Validation

- Amount must be greater than zero and no more than $50,000.
- Transactions over $10,000 require identity verification (`verified=True`).

## Development

```
pip install pytest
pytest
```
