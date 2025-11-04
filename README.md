# FX Profit Calculator - Web Application

A Python Flask web application that processes FX trading data from the AM sheet of "FX October PnL updated.xlsx" and provides real-time profit calculations with the ability to adjust buy and sell rates.

## Features

✅ **Real-time Calculations** - Updates profit calculations instantly as you adjust rates
✅ **Rate Adjustments** - Modify buy and sell rates with 4 decimal precision
✅ **Trade Type Detection** - Automatically identifies SELL or BUY trades based on values
✅ **Mark Up Display** - Shows the spread between your rate and bank rate
✅ **Total Profit Aggregation** - Displays total profit across all 22 trading days
✅ **Reset Functionality** - Restore all rates to original values
✅ **Visual Indicators** - Color-coded profit display (green for positive, red for negative)

## Requirements

- Python 3.7 or higher
- Flask
- openpyxl
- numpy

## Installation

1. Navigate to the project directory:
```bash
cd C:\Users\Admin\Desktop\MYProject\FXSimulation
```

2. Install required packages (if not already installed):
```bash
python -m pip install flask openpyxl numpy
```

## How to Run

### Option 1: Using the run script
```bash
python run.py
```
This will start the Flask server and automatically open your browser to http://localhost:5000

### Option 2: Direct Flask execution
```bash
python app.py
```
Then open your browser and navigate to http://localhost:5000

## How to Use the Application

1. **View Trading Data**: The table displays all 22 trading days with their rates and profit calculations

2. **Adjust Buy Rate**: 
   - Click the "Buy Rate" input field for any trading day
   - Enter a new rate (up to 4 decimal places)
   - Press Enter or click away to apply the change
   - The profit calculation updates in real-time

3. **Adjust Sell Rate**:
   - Click the "Sell Rate" input field for any trading day
   - Enter a new rate (up to 4 decimal places)
   - Press Enter or click away to apply the change
   - The profit calculation updates immediately

4. **Reset All Rates**:
   - Click the "Reset All Rates" button
   - Confirm the action in the dialog
   - All rates return to their original values and profit recalculates

## Calculation Logic

### Daily Profit Calculation
```
Profit = Buy Value - Sell Value - Bank Value

Where:
- Buy Value = Buy Rate × Buy Amount
- Sell Value = Sell Rate × Sell Amount
- Bank Value = Bank Rate × Bank Amount (Fixed - cannot be adjusted)
```

### Trade Type Detection
```
IF Sell Value > Buy Value
  THEN Trade Type = "SELL"
ELSE
  Trade Type = "BUY"
```

### Mark Up Calculation
```
IF Trade Type = "SELL"
  THEN Mark Up = Sell Rate - Bank Rate
ELSE (Trade Type = "BUY")
  THEN Mark Up = Buy Rate - Bank Rate
```

### Total Profit
The sum of all daily profits for the 22 trading days (Sep 30 - Oct 30, 2025)

## Data Source

- **File**: FX October PnL updated.xlsx
- **Sheet**: AM (AM session data only)
- **Trading Days**: 22 days
- **Date Range**: October 1-30, 2025

## Project Files

- `app.py` - Main Flask application with calculation logic
- `run.py` - Simple runner script to start the application
- `templates/index.html` - Web interface with styling and JavaScript
- `inspect_excel.py` - Utility to inspect Excel file structure
- `test_calculator.py` - Unit test for the calculator
- `fx_profit_calc_logic.md` - Detailed documentation of calculation logic

## Troubleshooting

### Port already in use
If port 5000 is already in use, modify the port in `app.py` or `run.py`:
```python
app.run(debug=True, port=5001)  # Use port 5001 instead
```

### Excel file not found
Ensure the Excel file is in the same directory as the Python files:
```
C:/Users/Admin/Desktop/MYProject/FXSimulation/FX October PnL updated.xlsx
```

### Module not found errors
Install missing packages:
```bash
python -m pip install flask openpyxl numpy
```

## Technical Details

- **Backend**: Python Flask (RESTful API)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data Processing**: openpyxl for Excel file reading
- **Calculation Engine**: Native Python with numpy support
- **Real-time Updates**: AJAX/Fetch API for seamless data updates

## API Endpoints

- `GET /` - Main application page
- `GET /api/get-data` - Retrieve current data and calculations
- `POST /api/update-rate` - Update a buy or sell rate
- `POST /api/reset` - Reset all rates to original values

## Browser Compatibility

- Chrome/Chromium (Latest)
- Firefox (Latest)
- Safari (Latest)
- Edge (Latest)

## Notes

- Bank rates are fixed and cannot be adjusted
- All amounts (USD) are fixed per trading day
- Rates can be adjusted with up to 4 decimal places precision
- All calculations are done on the server side for accuracy
