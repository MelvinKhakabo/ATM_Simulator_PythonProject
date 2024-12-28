# ATM_Simulator_PythonProject

A command-line ATM simulator that allows users to perform basic banking operations such as checking their balance, withdrawing money, depositing money, and exiting the system.

Features:
Menu Interface:

Display a menu with options:
Check Balance
Deposit Money
Withdraw Money
Exit
User Authentication:

Simulate a login process where the user enters a predefined PIN.
Allow 3 attempts before locking the system.
Functionalities:

Check Balance: Show the current account balance.
Deposit Money: Allow the user to add an amount to their balance.
Withdraw Money: Subtract an amount from the balance if sufficient funds are available.
Prevent withdrawal if the amount exceeds the balance.
Exit: End the program gracefully.
Data Handling:

Use a dictionary or variables to store user data (e.g., balance and PIN).
Optionally, allow saving and loading data from a text file.
Bonus Features (Optional):
Transaction History: Keep a log of all transactions (deposits, withdrawals) and display it when requested.
Multiple Accounts: Support multiple users with different PINs and balances.
Persistent Data: Save the user data (e.g., balances and transactions) to a file so it persists between program runs.