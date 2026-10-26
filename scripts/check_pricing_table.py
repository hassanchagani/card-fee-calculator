"""Fail if the pricing table in README.md does not match CARD_RATES.

Runs in CI so the published pricing never drifts from the code.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from card_fees.pricing import CARD_RATES  # noqa: E402

ROW = re.compile(r"^\|\s*(\w+)\s*\|\s*([\d.]+)%\s*\|\s*\$([\d.]+)\s*\|", re.MULTILINE)


def main():
    readme = (ROOT / "README.md").read_text()
    documented = {
        card: (round(float(pct) / 100, 6), round(float(fixed), 2))
        for card, pct, fixed in ROW.findall(readme)
    }
    actual = {
        card: (round(p["rate"], 6), round(p["fixed"], 2)) for card, p in CARD_RATES.items()
    }

    if documented != actual:
        print("README pricing table does not match card_fees/pricing.py")
        print(f"  README: {documented}")
        print(f"  Code:   {actual}")
        return 1

    print("Pricing table OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
