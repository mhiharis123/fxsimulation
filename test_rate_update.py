import sys
sys.path.insert(0, 'C:\\Users\\Admin\\Desktop\\MYProject\\FXSimulation')

from app import FXProfitCalculator
from datetime import datetime

calculator = FXProfitCalculator('FX October PnL updated.xlsx')

print("=" * 60)
print("BEFORE UPDATE")
print("=" * 60)

results_before, total_before = calculator.calculate_all_profits()
first_day_before = results_before[0]

print(f"\n{first_day_before['date']}:")
print(f"  Buy Rate: {first_day_before['buy_rate']}")
print(f"  Sell Rate: {first_day_before['sell_rate']}")
print(f"  Profit: RM {first_day_before['profit']:.2f}")

print(f"\nTotal Profit: RM {total_before:.2f}")

# Simulate rate update from frontend
print("\n" + "=" * 60)
print("UPDATING RATES")
print("=" * 60)

test_date = '2025-10-01'
new_buy_rate = 4.215  # Changed from 4.221
new_sell_rate = 4.190  # Changed from 4.196

calculator.adjustments[test_date] = {
    'buy': new_buy_rate,
    'sell': new_sell_rate
}

print(f"\nUpdated {test_date}:")
print(f"  New Buy Rate: {new_buy_rate}")
print(f"  New Sell Rate: {new_sell_rate}")

# Recalculate
results_after, total_after = calculator.calculate_all_profits()
first_day_after = results_after[0]

print("\n" + "=" * 60)
print("AFTER UPDATE")
print("=" * 60)

print(f"\n{first_day_after['date']}:")
print(f"  Buy Rate: {first_day_after['buy_rate']}")
print(f"  Sell Rate: {first_day_after['sell_rate']}")
print(f"  Profit: RM {first_day_after['profit']:.2f}")

print(f"\nTotal Profit: RM {total_after:.2f}")

# Verify the change
print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)
print(f"\nProfit changed: {first_day_before['profit']:.2f} → {first_day_after['profit']:.2f}")
print(f"Difference: RM {first_day_after['profit'] - first_day_before['profit']:.2f}")

if first_day_after['profit'] != first_day_before['profit']:
    print("\n✅ SUCCESS: Rates updated and profit recalculated correctly!")
else:
    print("\n❌ FAILED: Profit did not change after rate update!")
