"""Command line entry point: python -m card_fees AMOUNT [CARD_TYPE] [--verified]"""

import argparse
import sys

from card_fees import ValidationError, calculate_fee


def main(argv=None):
    parser = argparse.ArgumentParser(description="Calculate a card processing fee.")
    parser.add_argument("amount", type=float, help="Transaction amount in dollars")
    parser.add_argument("card_type", nargs="?", default="standard")
    parser.add_argument("--verified", action="store_true", help="Cardholder identity verified")
    args = parser.parse_args(argv)

    try:
        fee = calculate_fee(args.amount, args.card_type, verified=args.verified)
    except ValidationError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1

    print(f"${fee:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
