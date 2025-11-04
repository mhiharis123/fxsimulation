import openpyxl

file_path = 'FX October PnL updated.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb['PM']

print("Examining PM Sheet structure more carefully")
print("=" * 100)

# Show rows around row 249 to understand the structure
print("Rows 245-265 (showing all columns A through M):")
for row_num in range(245, 266):
    row = ws[row_num]
    values = [cell.value for cell in row]
    print(f"Row {row_num}: {values}")
