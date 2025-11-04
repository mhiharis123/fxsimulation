import sys
sys.path.insert(0, 'C:\\Users\\Admin\\Desktop\\MYProject\\FXSimulation')

from app import FXProfitCalculatorPM
from datetime import datetime

calculator_pm = FXProfitCalculatorPM('FX October PnL updated.xlsx')

print("Checking USD/MYR transactions in detail")
print("=" * 80)

results, total_profit = calculator_pm.calculate_all_profits()

# Filter USD/MYR transactions
usd_transactions = [r for r in results if r['currency'] == 'USD/MYR']

print(f"Total USD/MYR transactions: {len(usd_transactions)}")
print("\nAll USD/MYR transactions:")
for i, r in enumerate(usd_transactions, 1):
    print(f"{i}. Date: {r['date']}, Trade Type: {r['trade_type']}, Profit: RM {r['profit']:.2f}")

print("\n" + "=" * 80)
print("Checking if 2025-10-07 USD/MYR is in the data:")
oct_7_usd = [r for r in results if r['date'] == '2025-10-07' and r['currency'] == 'USD/MYR']
if oct_7_usd:
    print("Found! Details:")
    for r in oct_7_usd:
        print(f"  Profit: RM {r['profit']:.2f}")
else:
    print("NOT FOUND - 2025-10-07 USD/MYR is missing!")
    print("\nAll transactions on 2025-10-07:")
    oct_7_all = [r for r in results if r['date'] == '2025-10-07']
    for r in oct_7_all:
        print(f"  {r['currency']}: Profit RM {r['profit']:.2f}")
