#Authentication before using the ATM
attempts = 3
pin = "1234"
while attempts > 0:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print(f"Invalid PIN. {attempts} attempts left.")
else:
    print("Too many invalid attempts. Access denied.")
    exit()
