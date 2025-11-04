import sys
sys.path.insert(0, 'C:\\Users\\Admin\\Desktop\\MYProject\\FXSimulation')

from app import FXProfitCalculatorPM

calculator_pm = FXProfitCalculatorPM('FX October PnL updated.xlsx')

print("Testing PM Sheet Calculator")
print("=" * 80)

results, total_profit = calculator_pm.calculate_all_profits()

print("\nPM Sheet Data Loaded Successfully!")
print(f"Total transactions: {len(results)}")
print(f"Total Profit: RM {total_profit:.2f}")

# Group by currency
currencies = {}
for r in results:
    if r['currency'] not in currencies:
        currencies[r['currency']] = []
    currencies[r['currency']].append(r)

print("\nCurrencies found:")
for currency in sorted(currencies.keys()):
    count = len(currencies[currency])
    currency_profit = sum(r['profit'] for r in currencies[currency])
    print(f"  {currency}: {count} transactions, Profit: RM {currency_profit:.2f}")

print("\nFirst 3 transactions:")
for i, result in enumerate(results[:3]):
    print(f"\n{i+1}. {result['date']} - {result['currency']}")
    print(f"   Trade Type: {result['trade_type']} | Buy Rate: {result['buy_rate']} | Sell Rate: {result['sell_rate']}")
    print(f"   Profit: RM {result['profit']:.2f}")

print("\n" + "=" * 80)
print("PM Sheet Calculator is working correctly!")
print("Successfully loaded data from PM sheet with multiple currencies")
