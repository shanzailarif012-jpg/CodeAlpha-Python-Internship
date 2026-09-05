# Stock Portfolio Tracker

A simple Python command-line tool to track stock investments using hardcoded stock prices. Built as **Project 1** for the CodeAlpha Python Internship.

## 📌 Description

This program lets a user build a stock portfolio by entering stock names and quantities. It calculates the total investment value based on a predefined dictionary of stock prices, displays a summary, and optionally saves the results to a text file.

## ✨ Features

- Displays available stock names to choose from
- Accepts stock name and quantity input in a loop (type `done` to finish)
- Validates input (handles invalid stock names and invalid/negative quantities)
- Calculates per-stock investment value and total portfolio investment
- Displays a clean summary of the portfolio
- Optionally saves the summary to a `.txt` file

## 🛠️ Concepts Used

- Dictionaries (storing and looking up stock prices)
- Input/output handling
- `while` loops and `break`/`continue`
- `try`/`except` for error handling
- String methods (`.strip()`, `.lower()`, `.upper()`, `.join()`)
- File handling (`open()`, `.write()`, `with` statement)

## ▶️ How to Run

```bash
python3 stock_portfolio_tracker.py
```

Follow the prompts:
1. Enter a stock name from the displayed list
2. Enter the quantity of shares
3. Repeat, or type `done` to finish
4. View your portfolio summary and total investment
5. Choose whether to save the results to a file

## 📂 Sample Stocks

| Stock | Price (PKR) |
|---|---|
| Suzuki Alto VXR 2026 | 3,050,000 |
| Toyota Corolla Grande 2026 | 8,000,000 |
| Honda City 1.2 2026 | 4,950,000 |

## 📄 Output

If the user chooses to save results, a `portfolio_result.txt` file is generated containing the portfolio summary and total investment.

## 👤 Author
Github = https://github.com/shanzailarif012-jpg
CodeAlpha Python Internship — Project 1