# CodeAlpha - Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 180,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("=" * 45)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

print("\nEnter 'done' when you have finished.")

# Get stock information from the user
while True:
    stock = input("\nEnter stock symbol: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    investment = stock_prices[stock] * quantity

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += investment

    print(f"Added {quantity} shares of {stock}.")
    print(f"Investment: ${investment:,.2f}")

# Display portfolio summary
print("\n" + "=" * 45)
print("           PORTFOLIO SUMMARY")
print("=" * 45)

if not portfolio:
    print("No stocks were added.")
else:
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        print(f"{stock}: {quantity} shares = ${value:,.2f}")

    print("-" * 45)
    print(f"Total Investment: ${total_investment:,.2f}")

# Save portfolio to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(
            f"{stock}: {quantity} shares = ${value:,.2f}\n"
        )

    file.write("\n")
    file.write(f"Total Investment: ${total_investment:,.2f}\n")

print("\nPortfolio saved to portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")
