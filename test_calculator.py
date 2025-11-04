import sys
sys.path.insert(0, 'C:\\Users\\Admin\\Desktop\\MYProject\\FXSimulation')

from app import FXProfitCalculator
from datetime import datetime

calculator = FXProfitCalculator('FX October PnL updated.xlsx')

print("Loaded data for days:", len(calculator.data))

results, total_profit = calculator.calculate_all_profits()

print(f"\nTotal days: {len(results)}")
print(f"Total Profit: RM {total_profit:.2f}")

print("\nFirst 3 days:")
for i, result in enumerate(results[:3]):
    print(f"\n{result['date']}:")
    print(f"  Buy Rate: {result['buy_rate']}")
    print(f"  Sell Rate: {result['sell_rate']}")
    print(f"  Profit: RM {result['profit']:.2f}")
    print(f"  Trade Type: {result['trade_type']}")
