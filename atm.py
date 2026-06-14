class ATM:
    def __init__(self):
        self.pin = 1234
        self.balance = 5000

    def withdraw(self):
        amount = int(input("Enter withdrawal amount: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.balance += amount
        print("Deposit Successful")
        print("Current Balance:", self.balance)

    def change_pin(self):
        new_pin = int(input("Enter new PIN: "))
        confirm_pin = int(input("Re-enter new PIN: "))

        if new_pin == confirm_pin:
            self.pin = new_pin
            print("PIN changed successfully")
        else:
            print("PINs do not match")

    def check_balance(self):
        print("Current Balance:", self.balance)


atm = ATM()

password = int(input("Enter your PIN: "))

if password ==atm.pin:

    while True:
        print(" CUB BANK ATM ")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Change PIN")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.withdraw()

        elif choice == 2:
            atm.deposit()

        elif choice == 3:
            atm.change_pin()

        elif choice == 4:
            atm.check_balance()

        elif choice == 5:
            print("Thank You for Using CUB Bank ATM")
            break

        else:
            print("Invalid Choice. Please select 1 to 5.")

else:
    print("Incorrect PIN")
