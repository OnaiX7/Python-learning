
def user_action_menu():
    print("\nWelcome to Banking System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")
    choice = input("Enter your choice: \n")
    return choice

def show_balance():
    print(f"You account balance is ${account_balance:2f}")

def deposit():
    deposited_amount = (
        float(input("Enter the amount you want to deposit: $")))

    if deposited_amount < 0:
        print("Choose withdrawal to withdraw funds")
        return 0
    else:
        return deposited_amount

def withdraw():
    amount_to_withdraw = (
        float(input("Enter the amount you want to withdraw: $")))

    if amount_to_withdraw > account_balance:
        print(f"You don't have enough funds to withdraw ${amount_to_withdraw:.2f}!")
        return 0
    elif amount_to_withdraw < 0:
        print("Choose deposit to deposit funds")
        return 0
    else:
        return amount_to_withdraw

account_balance = float(0.0)
is_running = True

while is_running:
    choice = user_action_menu()

    match choice:
        case "1":
            account_balance += deposit()
        case "2":
            account_balance -= withdraw()
        case "3":
            show_balance()
        case "4":
            print("Thank you for using our Banking System")
            is_running = False
        case _:
            print("Please enter a valid choice")