import sys
sys.path.insert(0, 'C:\\Users\\Admin\\Desktop\\MYProject\\FXSimulation')

from app import FXProfitCalculator

calculator = FXProfitCalculator('FX October PnL updated.xlsx')

print("Testing Rate Update Fix")
print("-" * 60)

# Before update
results_before, total_before = calculator.calculate_all_profits()
first_day_before = results_before[0]

print("\nBEFORE UPDATE:")
print("Date: {}".format(first_day_before['date']))
print("Buy Rate: {}".format(first_day_before['buy_rate']))
print("Sell Rate: {}".format(first_day_before['sell_rate']))
print("Profit: RM {:.2f}".format(first_day_before['profit']))
print("Total Profit: RM {:.2f}".format(total_before))

# Apply adjustment
test_date = '2025-10-01'
calculator.adjustments[test_date] = {
    'buy': 4.215,
    'sell': 4.190
}

# After update
results_after, total_after = calculator.calculate_all_profits()
first_day_after = results_after[0]

print("\n" + "-" * 60)
print("AFTER RATE UPDATE:")
print("Date: {}".format(first_day_after['date']))
print("Buy Rate: {}".format(first_day_after['buy_rate']))
print("Sell Rate: {}".format(first_day_after['sell_rate']))
print("Profit: RM {:.2f}".format(first_day_after['profit']))
print("Total Profit: RM {:.2f}".format(total_after))

print("\n" + "-" * 60)
print("RESULT:")
profit_changed = first_day_after['profit'] != first_day_before['profit']
print("Profit updated: {}".format("YES" if profit_changed else "NO"))
print("Difference: RM {:.2f}".format(first_day_after['profit'] - first_day_before['profit']))

if profit_changed:
    print("\nSUCCESS: Rate updates are now working correctly!")
else:
    print("\nFAILED: Profit did not change!")
