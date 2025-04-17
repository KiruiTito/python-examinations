
QUESTION 2

def main():
    # Create an instance of BankAccount with a specific account number
    account = BankAccount("123456789")
    
    # Test deposit method
    account.deposit(5000)
    
    # Test withdraw method
    account.withdraw(2000)
    
    # Get and print the final balance
    account.get_balance()

if __name__ == "__main__":
    main()
