# ATM_Simulator_PythonProject

A command-line ATM simulator that allows users to perform basic banking operations such as checking their balance, withdrawing money, depositing money, and exiting the system.

## Features:
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


## Sample interaction
Welcome to Simple ATM Simulator!
Please enter your PIN: ****
Login Successful!
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option: 1
Your current balance is $500.
Choose an option: 2
Enter the amount to deposit: 200
$200 deposited successfully. New balance: $700.
Choose an option: 3
Enter the amount to withdraw: 300
$300 withdrawn successfully. Remaining balance: $400.
Choose an option: 4
Thank you for using Simple ATM Simulator. Goodbye!
