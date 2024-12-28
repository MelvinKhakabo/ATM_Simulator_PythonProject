#ATM menu
while True:
    print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        # Add functionality for checking balance here
        print("You chose to check your balance.")
    elif choice == "2":
        # Add functionality for depositing money here
        print("You chose to deposit money.")
    elif choice == "3":
        # Add functionality for withdrawing money here
        print("You chose to withdraw money.")
    elif choice == "4":
        print("Thank you for using the ATM Simulator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

