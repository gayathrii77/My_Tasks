CodeAlpha Stock Portfolio Tracker

A simple Python program that calculates the total investment value of a user's stock portfolio.

This project was developed as part of the CodeAlpha Python Programming Internship.

📌 Project Overview

The Stock Portfolio Tracker allows users to enter stock symbols and the number of shares they own.

The program uses predefined stock prices to calculate the investment value of each stock and the total value of the portfolio.

The portfolio report is also saved to a portfolio.txt file.

✨ Features
Displays available stocks and their prices
Accepts stock symbols from the user
Accepts the quantity of shares
Calculates individual investment values
Calculates total portfolio investment
Supports multiple stocks
Validates stock symbols
Validates quantity input
Saves the portfolio report to a text file
🛠️ Technologies Used
Python 3
Dictionaries
Loops
Conditional statements
User input/output
File handling
Basic arithmetic
📂 Project Structure
CodeAlpha_StockPortfolioTracker/
│
├── portfolio_tracker.py
├── portfolio.txt
└── README.md

💰 Available Stocks

The program currently uses the following predefined stock prices:

Stock	Price
AAPL	$180
TSLA	$250
GOOGL	$140
AMZN	$180
MSFT	$420
▶️ How to Run

Open the terminal inside the project folder and run:

python portfolio_tracker.py


Enter the stock symbol and quantity when prompted.

Enter:

done


when you have finished adding stocks.

🧪 Example
=============================================
        STOCK PORTFOLIO TRACKER
=============================================

Available Stocks:
AAPL - $180
TSLA - $250
GOOGL - $140
AMZN - $180
MSFT - $420

Enter 'done' when you have finished.

Enter stock symbol: AAPL
Enter quantity of AAPL: 5
Added 5 shares of AAPL.
Investment: $900.00

Enter stock symbol: TSLA
Enter quantity of TSLA: 3
Added 3 shares of TSLA.
Investment: $750.00

Enter stock symbol: DONE

=============================================
           PORTFOLIO SUMMARY
=============================================
AAPL: 5 shares = $900.00
TSLA: 3 shares = $750.00
---------------------------------------------
Total Investment: $1,650.00

Portfolio saved to portfolio.txt
Thank you for using Stock Portfolio Tracker!

📄 Output File

The program creates portfolio.txt containing a summary of the user's portfolio and total investment.

🎯 CodeAlpha Task

Task 2 — Stock Portfolio Tracker

This project fulfills the CodeAlpha requirement to create a stock portfolio tracker using a hardcoded stock-price dictionary, user input, and basic calculations.

👨‍💻 Author

Developed for the CodeAlpha Python Programming Internship.