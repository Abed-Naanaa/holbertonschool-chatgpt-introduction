class Checkbook:
    def __init__(self):
        """
        Initializes the Checkbook class with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook balance.

        Args:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook balance.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance of the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function that interacts with the user to perform deposit, withdraw, and check balance operations.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            while True:  # Loop until valid input is received
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    cb.deposit(amount)
                    break  # Exit loop after valid deposit
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            while True:  # Loop until valid input is received
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    cb.withdraw(amount)
                    break  # Exit loop after valid withdrawal
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
