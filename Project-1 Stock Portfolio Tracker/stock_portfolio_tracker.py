# Project- 1 Stock_Portfolio_Tracker

stock_prices = {
    "suzuki alto vxr 2026" : 3050000,
    "toyota carolla grande 2026" : 8000000,
    "honda city 1.2 2026" : 4950000,
    
}

portfolio = {} # Empty Dict

print(", ".join(stock_prices.keys()).upper()) # Print Stock Names


while True:
    user_stock_name = input("Enter Stock Name: ").strip().lower()
    if user_stock_name == "done":
        break

    if user_stock_name not in stock_prices:
        print("Error Not Found")
        continue
    
    user_quantity = input("Enter Quantity: ")
    try:
        user_quantity = int(user_quantity)
        if user_quantity <= 0:
            print("quantity must be positive")
            continue
    except ValueError:
        print("invalid number")
        continue
    portfolio[user_stock_name] = portfolio.get(user_stock_name, 0) + user_quantity
    print(f"Added {user_quantity} Units of {user_stock_name}")

if portfolio == {}:
    print("No Stocks Added")
    exit()

total_investment = 0
investment_details = {}

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    investment_details[stock] = value
    total_investment = total_investment + value

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = investment_details[stock]
    print(f"{stock}: {quantity} Units x {price} = {value}")

print(f"Total Investement: {total_investment}")

result_save = input("save result to file? (yes/no): ").strip().lower()
if result_save == "yes":
    with open ("portfolio_result.txt" , "w") as f:
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = investment_details[stock]
            f.write(f"{stock}: {quantity} Units x {price} = {value}\n")

        f.write(f"Total Investment: {total_investment}\n")

