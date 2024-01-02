from Bank import Bank, Admin, User
bank = Bank()
admin = Admin()

while True:
    print("\nBanking Management System:")
    print("1. Admin Portal")
    print("2. User Portal")
    print("3. Exit")

    if (choice := input("Enter your choice: ")) == "1":
        if (admin_password := input("Enter admin password (admin): ")) == "admin":
            print("\nAdmin Menu:")
            print("1. Create User Account")
            print("2. Delete User Account")
            print("3. See All User Accounts")
            print("4. Check Bank Balance")
            print("5. Check Total Loan Amount")
            print("6. Turn Loan Feature On/Off")
            print("7. Logout")

            if (admin_option := input("Enter your choice: ")) == "1":
                name = input("Enter user's name: ")
                email = input("Enter user's email: ")
                address = input("Enter user's address: ")
                account_type = input("Enter account type (Savings/Current): ")
                account = bank.create_user_account(name, email, address, account_type)
                print(f"Account created successfully. Account Number: {account.account_number}")
            elif admin_option == "2":
                account_number = int(input("Enter user's Account Number to delete: "))
                if bank.delete_user_account(account_number):
                    print(f"User Account {account_number} deleted successfully.")
                else:
                    print("User Account not found.")
            elif admin_option == "3":
                user_accounts = bank.see_all_user_accounts()
                print("User Accounts:")
                for account_number, user in user_accounts.items():
                    print(f"Account Number: {account_number}, Name: {user.name}")
            elif admin_option == "4":
                print(f"Bank Balance: ${bank.check_bank_balance()}")
            elif admin_option == "5":
                print(f"Total Loan Amount: ${bank.check_total_loan_amount()}")
            elif admin_option == "6":
                bank.toggle_loan_feature()
                status = "on" if bank.loan_status else "off"
                print(f"Loan feature turned {status}.")
            elif admin_option == "7":
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Admin login failed. Incorrect password.")
    elif choice == "2":
        user_option = input("1. Login\n2. Register\n3. Back to previous\nEnter your choice: ")
        if user_option == "1":
            account_number = int(input("Enter your account number: "))
            user = bank.see_all_user_accounts().get(account_number)
            if user:
                print(f"Welcome, {user.name}!")
                while True:
                    print("\nUser Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Take a Loan")
                    print("6. Transfer Money")
                    print("7. Logout")
                    user_option = input("Enter your choice: ")

                    if user_option == "1":
                        amount = float(input("Enter the amount to deposit: "))
                        user.deposit(amount)
                        print(f"${amount} deposited successfully.")
                    elif user_option == "2":
                        amount = float(input("Enter the amount to withdraw: "))
                        result = user.withdraw(amount)
                        if result == "Withdrawal amount exceeded":
                            print(result)
                        else:
                            print(f"${amount} withdrawn successfully.")
                    elif user_option == "3":
                        print(f"Available balance: ${user.check_balance()}")
                    elif user_option == "4":
                        print("Transaction History:")
                        for transaction in user.check_transaction_history():
                            print(transaction)
                    elif user_option == "5":
                        if user.can_take_loan():
                            loan_amount = float(input("Enter the loan amount: "))
                            result = bank.take_loan(user, loan_amount)
                            if result:
                                print(f"Loan of ${loan_amount} granted successfully.")
                            else:
                                print("Loan service is currently unavailable or insufficient bank balance.")
                        else:
                            print("You have already taken the maximum number of loans (2).")
                    elif user_option == "6":
                        target_account = int(input("Enter the target account number: "))
                        target_user = bank.see_all_user_accounts().get(target_account)
                        if target_user:
                            amount = float(input("Enter the amount to transfer: "))
                            result = user.transfer_money(target_user, amount)
                            if result == "Insufficient balance for the transfer":
                                print(result)
                            else:
                                print(f"${amount} transferred successfully to Account {target_account}.")
                        else:
                            print("Account does not exist.")
                    elif user_option == "7":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Account not found. Please register.")
        elif user_option == "2":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter your account type (Savings/Current): ")
            user = bank.create_user_account(name, email, address, account_type)
            print(f"Account created successfully. Account Number: {user.account_number}")
        elif user_option == "3":
            continue
        else:
            print("Invalid choice. Please try again.")
    elif choice == "3":
        print("Thank you for using the Banking Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
