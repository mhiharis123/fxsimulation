import openpyxl
from datetime import datetime

file_path = 'FX October PnL updated.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb['PM']

print("Debugging the load_data function for rows 248-260")
print("=" * 100)

daily_data = {}
current_currency = None
current_date = None

for row_idx in range(248, 261):
    row = ws[row_idx]
    values = [cell.value for cell in row]
    
    trade_date = values[0]
    currency_col_i = values[8]
    direction = values[9]
    rate = values[10]
    amount = values[11]
    value = values[12]
    
    print(f"\nRow {row_idx}:")
    print(f"  Date: {trade_date}, ColI: {currency_col_i}, Direction: {direction}")
    
    # Skip header rows and empty rows
    if not direction:
        print(f"  SKIP: no direction")
        continue
    if trade_date is None and direction not in ['BUY', 'SELL', 'BANK']:
        print(f"  SKIP: date=None and direction not in BUY/SELL/BANK")
        continue
    
    # Skip separator rows
    if isinstance(currency_col_i, str) and '-' in currency_col_i:
        print(f"  SKIP: separator row")
        continue
    
    # Update current currency and date when we see a currency in column I
    if currency_col_i and isinstance(currency_col_i, str) and currency_col_i not in ['', 'TOTAL PROFIT:']:
        current_currency = currency_col_i
        if trade_date:
            current_date = trade_date
        print(f"  UPDATE: currency={current_currency}, date={current_date}")
    
    # Only process BUY, SELL, BANK directions
    if direction not in ['BUY', 'SELL', 'BANK']:
        print(f"  SKIP: direction not in BUY/SELL/BANK")
        continue
    
    # Use current date if trade_date is None
    effective_date = trade_date if trade_date else current_date
    
    # Create key
    key = (effective_date, current_currency)
    
    if key not in daily_data:
        daily_data[key] = {}
    
    print(f"  PROCESS: key=({effective_date}, {current_currency}), direction={direction}")
    
    if direction == 'BUY':
        daily_data[key]['BUY'] = {'rate': rate, 'amount': amount, 'value': value}
    elif direction == 'SELL':
        daily_data[key]['SELL'] = {'rate': rate, 'amount': amount, 'value': value}
    elif direction == 'BANK':
        daily_data[key]['BANK'] = {'rate': rate, 'amount': amount, 'value': value}

print("\n" + "=" * 100)
print("Final daily_data keys:")
for key in sorted(daily_data.keys()):
    print(f"  {key}: {list(daily_data[key].keys())}")
