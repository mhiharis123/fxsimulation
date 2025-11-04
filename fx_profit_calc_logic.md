# FX Profit Calculator - Application Logic

## Overview
This application allows users to simulate and analyze FX trading profits by adjusting Buy and Sell rates while keeping the Bank rate fixed. It calculates daily profits and provides a total profit summary for all trading days.

---

## Data Structure

### Input Data
Each trading day contains the following information:

```
{
  date: string (YYYY-MM-DD format),
  BUY: {
    rate: number (original buy rate),
    amount: number (base USD amount),
    value: number (original buy value = rate × amount)
  },
  SELL: {
    rate: number (original sell rate),
    amount: number (base USD amount),
    value: number (original sell value = rate × amount)
  },
  BANK: {
    rate: number (bank exchange rate - FIXED),
    amount: number (bank transaction amount),
    value: number (bank value = rate × amount)
  }
}
```

### Dataset
- **Total Trading Days**: 22 days
- **Date Range**: September 30, 2025 to October 30, 2025
- **AM Sheet Only**: All data sourced from the AM session sheet

---

## Core Calculations

### 1. Value Calculation
For any given rate and amount:
```
Value = Rate × Amount
```

### 2. Trade Type Detection
Determines if the trade is a SELL or BUY based on comparing values:

```
IF Sell Value > Buy Value
  THEN Trade Type = "SELL"
ELSE
  Trade Type = "BUY"
```

**Logic**: When the client sells to us at a higher value than we buy from the bank, it's a SELL trade (positive margin).

### 3. Profit Calculation
The profit for each day is calculated as:

```
Profit = Buy Value - Sell Value - Bank Value
```

**Component Breakdown**:
- **Buy Value**: Rate × Buy Amount (adjustable)
- **Sell Value**: Rate × Sell Amount (adjustable)
- **Bank Value**: Fixed Bank Rate × Bank Amount (NOT adjustable)

**Example**:
- Buy Value: 1,123,220.02
- Sell Value: 1,362,651.96
- Bank Value: -246,563.00
- Profit = 1,123,220.02 - 1,362,651.96 - (-246,563) = **7,131.06**

### 4. Mark Up Calculation
Mark up represents the spread between your rate and the bank rate:

```
IF Trade Type = "SELL"
  THEN Mark Up = Sell Rate - Bank Rate
ELSE (Trade Type = "BUY")
  THEN Mark Up = Buy Rate - Bank Rate
```

**Example**:
- If SELL trade: 4.1905 - 4.1985 = -0.0080 (negative markup)
- If BUY trade: 4.2281 - 4.2201 = 0.0080 (positive markup)

---

## User Interactions

### 1. Adjust Buy Rate
- User can modify the Buy Rate for any trading day
- Input accepts up to 4 decimal places (0.0001 precision)
- Changes affect:
  - Buy Value (recalculated as new rate × buy amount)
  - Trade Type (re-evaluated)
  - Profit (recalculated)
  - Mark Up (recalculated)

### 2. Adjust Sell Rate
- User can modify the Sell Rate for any trading day
- Input accepts up to 4 decimal places (0.0001 precision)
- Changes affect:
  - Sell Value (recalculated as new rate × sell amount)
  - Trade Type (re-evaluated)
  - Profit (recalculated)
  - Mark Up (recalculated)

### 3. Reset All Rates
- Button to restore all Buy and Sell rates to their original values
- Bank rates remain unchanged (they are fixed)
- Total profit returns to original calculation

---

## Real-Time Calculations

### Per-Row Calculation (For Each Trading Day)

```
FUNCTION calculateDayProfit(day, adjustments):
  buyRate = adjustments[day.date].BUY OR day.originalBuyRate
  sellRate = adjustments[day.date].SELL OR day.originalSellRate
  bankRate = day.BANK.rate (FIXED)
  
  buyValue = buyRate × day.BUY.amount
  sellValue = sellRate × day.SELL.amount
  bankValue = bankRate × day.BANK.amount
  
  isSellTrade = (sellValue > buyValue)
  
  markUp = isSellTrade 
    ? (sellRate - bankRate)
    : (buyRate - bankRate)
  
  profit = buyValue - sellValue - bankValue
  
  RETURN {
    date,
    buyRate,
    sellRate,
    bankRate,
    buyValue,
    sellValue,
    bankValue,
    profit,
    isSellTrade,
    markUp
  }
END FUNCTION
```

### Total Profit Calculation

```
FUNCTION calculateTotalProfit(allDays, adjustments):
  totalProfit = 0
  
  FOR EACH day IN allDays:
    dayCalculation = calculateDayProfit(day, adjustments)
    totalProfit += dayCalculation.profit
  END FOR
  
  RETURN totalProfit
END FUNCTION
```

---

## State Management

### Adjustments State
```
adjustments = {
  "2025-10-01": {
    BUY: 4.2160,
    SELL: 4.1910
  },
  "2025-10-02": {
    BUY: 4.2285,
    SELL: 4.2055
  },
  ...
}
```

- Only stores **modified** rates
- If a rate is not in adjustments, the original rate is used
- Allows efficient tracking of user changes

---

## Display Table Structure

| Column | Type | Editable | Formula |
|--------|------|----------|---------|
| Date | Text | No | From data |
| Buy Rate | Number | Yes | User input |
| Sell Rate | Number | Yes | User input |
| Bank Rate | Number | No | Fixed value |
| Mark Up | Number | No | See Mark Up Calculation |
| Trade Type | Badge | No | Sell Value > Buy Value |
| Profit | Currency | No | Buy Value - Sell Value - Bank Value |

---

## Summary Section

### Total Profit Display
```
Total Profit = SUM(Daily Profits for all 22 days)
```

- **Green color**: Profit ≥ 0
- **Red color**: Profit < 0
- **Format**: RM X,XXX.XX (Malaysian Ringgit with 2 decimals)

### Metadata
- Total number of trading days: 22
- Date range indicator: (Sep 30 + Oct 1-30)

---

## Key Features & Constraints

### Features
✅ Real-time calculation updates
✅ Per-day rate adjustment
✅ Automatic trade type detection
✅ Mark up spread display
✅ Total profit aggregation
✅ Reset functionality
✅ Visual profit indicators (green/red)

### Constraints
- Bank rates are **FIXED** and cannot be adjusted
- Only Buy and Sell rates can be modified
- Rates must be precise to 4 decimal places
- All amounts (USD) are fixed for each day
- Profit formula is always: Buy Value - Sell Value - Bank Value

---

## Example Scenario

### Original Data (2025-10-01)
```
Buy Rate: 4.2155  | Buy Amount: 266,450.01
Sell Rate: 4.1905 | Sell Amount: 325,176.46
Bank Rate: 4.1985 | Bank Amount: -58,726.45 (FIXED)

Calculations:
Buy Value = 4.2155 × 266,450.01 = 1,123,220.02
Sell Value = 4.1905 × 325,176.46 = 1,362,651.96
Bank Value = 4.1985 × (-58,726.45) = -246,563.00

Sell Value > Buy Value → Trade Type = SELL
Mark Up = 4.1905 - 4.1985 = -0.0080
Profit = 1,123,220.02 - 1,362,651.96 - (-246,563) = 7,131.06
```

### After User Adjustment (Sell Rate: 4.1910)
```
New Sell Rate: 4.1910 (changed from 4.1905)

New Calculations:
Buy Value = 1,123,220.02 (unchanged)
Sell Value = 4.1910 × 325,176.46 = 1,362,864.67 (increased)
Bank Value = -246,563.00 (unchanged)

Sell Value > Buy Value → Trade Type = SELL (still)
Mark Up = 4.1910 - 4.1985 = -0.0075 (less negative)
New Profit = 1,123,220.02 - 1,362,864.67 - (-246,563) = 6,918.35 (decreased)
```

**Impact**: A 0.0005 increase in Sell Rate reduced profit by RM 212.71

---

## Summary
This app provides an interactive simulation tool for FX traders to understand how rate adjustments impact profitability, with real-time calculations across all trading days and comprehensive profit analytics.