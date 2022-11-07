"""
In this ROI Calculator program, I was able to go back on an issue I had in an earlier OOP homework (Video class exercise).
Previously, I was unable to figure out how to create unique user dictionaries without it overwriting other users data.
I was able to successfully implement that into my code this time! (yay)
The user is able to change/add users at any time without it affecting their own data.
At first I tried initializing the dictionaries inside the __init__ but kept getting issues where self.current_user wasn't getting updated
when the user changed to a different user.
Therefore I initialized inside the add_user method -- not sure if that's the correct or most efficient way to do it or if it was just brute force.
However I'm super happy with how this came out! Any constructive criticism is greatly appreciated so I can improve!

"""

from time import sleep

class ROI_Calculator():

    def __init__ (self):
        self.current_user = None
        self.user_info_dict = {}

    # Add user to master user dictionary including each specific user's income/expenses/investment dictionaries
    def add_user(self):
        name = input("Please start creating a new profile by entering a name: ")
        self.current_user = name.title().strip()
        self.user_info_dict[self.current_user] = {}
        self.user_info_dict[self.current_user]["Income"] = {}
        self.user_info_dict[self.current_user]["Expenses"] = {}
        self.user_info_dict[self.current_user]["Investments"] = {}
        self.user_info_dict[self.current_user]["Total Income"] = 0
        self.user_info_dict[self.current_user]["Total Expenses"] = 0
        self.user_info_dict[self.current_user]["Total Investments"] = 0
        self.user_info_dict[self.current_user]["Total Cash Flow"] = 0
        self.choose_user()

    # Choose user from master user dictionary
    def choose_user(self):
        while True:
            print("Users:")
            for user in self.user_info_dict:
                print(f"  {user}")
            current = input("Choose a user: ")
            if current.title().strip() in self.user_info_dict:
                self.current_user = current.title().strip()
                self.current_user_dict = self.user_info_dict[self.current_user]
                self.income_dict = self.current_user_dict["Income"]
                self.expenses_dict = self.current_user_dict["Expenses"]
                self.invest_dict = self.current_user_dict["Investments"]
                break
            else:
                print(f"{current} is not a valid user.")

    # Add items to current user's income dictionary
    def add_income(self):
        income_type = input("Please enter the type of income: ")
        income_type = income_type.title().strip()
        income_amt = input(f"Please enter the monthly {income_type} Income amount: $")
        income_amt = int(income_amt.replace(",", ""))
        self.income_dict[income_type] = income_amt
        self.user_info_dict[self.current_user]["Total Income"] += income_amt
        print(f"\nYour {income_type} Income has been added, {self.current_user}!")

    # Remove items from current user's income dictionary
    def remove_income(self):
        while True:
            income_type = input("Which type of income would you like to remove? ")
            income_type = income_type.title().strip()
            if income_type not in self.income_dict:
                print(f"\n{income_type} not found within your income. Please try again.")
            else:
                print(f"\nYour {income_type} Income has been removed, {self.current_user}.")
                self.user_info_dict[self.current_user]["Total Income"] -= self.income_dict[income_type]
                del self.income_dict[income_type]
                break

    # Edit items in current user's income dictionary
    def edit_income(self):
        while True:
            income_type = input("Which income type would you like to edit? ")
            income_type = income_type.title().strip()
            if income_type not in self.income_dict:
                print(f"\n{income_type} not found within your income. Please try again.")
            else:
                income_amt = input(f"Please enter the new monthly {income_type} Income amount: $")
                income_amt = int(income_amt.replace(",", ""))
                self.user_info_dict[self.current_user]["Total Income"] -= self.income_dict[income_type]
                self.user_info_dict[self.current_user]["Total Income"] += income_amt
                self.income_dict[income_type] = income_amt
                print(f"\nYour {income_type} Income has been updated, {self.current_user}!")
                break

    # Show items in current user's income dictionary and current user's total income
    def show_income(self):
        self.total_income = self.user_info_dict[self.current_user]["Total Income"]
        print(f"\nHere is a breakdown of {self.current_user}'s total monthly income:")
        for income_type, amount in self.income_dict.items():
            print(f"\t{income_type} = ${amount:,}")
        print(f"Total monthly income = ${self.total_income:,}")
        sleep(2)

    # Income main menu
    def calc_income(self):
        while True:
            print("""
            Income Options:
              [1] Add Income
              [2] Remove Income
              [3] Edit Income
              [4] Show Total Income
              [5] Return to Main Menu
            """)
            response = input("What would you like to do? ")
            if response == '1':
                self.add_income()
            elif response == '2':
                self.remove_income()
            elif response == '3':
                self.edit_income()
            elif response == '4':
                self.show_income()
            elif response == '5':
                break
            else:
                print("Invalid input. Please try again.")

    # Add expense to current user's expenses dictionary
    def add_expense(self):
        expense_type = input("Please enter the type of expense: ")
        expense_type = expense_type.title().strip()
        expense_amt = input(f"Please enter the monthly {expense_type} Expense amount: $")
        expense_amt = int(expense_amt.replace(",", ""))
        self.expenses_dict[expense_type] = expense_amt
        self.user_info_dict[self.current_user]["Total Expenses"] += expense_amt
        print(f"\nYour {expense_type} Expense has been added, {self.current_user}!")

    # Remove expense from current user's expenses dictionary
    def remove_expense(self):
        while True:
            expense_type = input("Which type of expense would you like to remove? ")
            expense_type = expense_type.title().strip()
            if expense_type not in self.expenses_dict:
                print(f"\n{expense_type} not found within your expenses. Please try again.")
            else:
                print(f"\nYour {expense_type} Expense has been removed, {self.current_user}.")
                self.user_info_dict[self.current_user]["Total Expenses"] -= self.expenses_dict[expense_type]
                del self.expenses_dict[expense_type]
                break

    # Edit expense in current user's expenses dictionary
    def edit_expense(self):
        while True:
            expense_type = input("Which expense type would you like to edit? ")
            expense_type = expense_type.title().strip()
            if expense_type not in self.expenses_dict:
                print(f"\n{expense_type} not found within your expenses. Please try again.")
            else:
                expense_amt = input(f"Please enter the new monthly {expense_type} Expense amount: $")
                expense_amt = int(expense_amt.replace(",", ""))
                self.user_info_dict[self.current_user]["Total Expenses"] -= self.expenses_dict[expense_type]
                self.user_info_dict[self.current_user]["Total Expenses"] += expense_amt
                self.expenses_dict[expense_type] = expense_amt
                print(f"\nYour {expense_type} Expense has been updated, {self.current_user}!")
                break

    # Show items in current user's expenses dictionary and current user's total expenses
    def show_expenses(self):
        self.total_expense = self.user_info_dict[self.current_user]["Total Expenses"]
        print(f"\nHere is a breakdown of {self.current_user}'s total monthly expenses:")
        for expense_type, amount in self.expenses_dict.items():
            print(f"\t{expense_type} = ${amount:,}")
        print(f"Total monthly expenses = ${self.total_expense:,}")
        sleep(2)

    # Expenses main menu
    def calc_expenses(self):
        while True:
            print("""
            Expenses Options:
              [1] Add Expense
              [2] Remove Expense
              [3] Edit Expense
              [4] Show Total Expenses
              [5] Return to Main Menu
            """)
            response = input("What would you like to do? ")
            if response == '1':
                self.add_expense()
            elif response == '2':
                self.remove_expense()
            elif response == '3':
                self.edit_expense()
            elif response == '4':
                self.show_expenses()
            elif response == '5':
                break
            else:
                print("Invalid input. Please try again.")
    
    # Calculate current user's cash flow by subtracting total expense from total income
    def calc_cash_flow(self):
        self.total_income = self.user_info_dict[self.current_user]["Total Income"]
        self.total_expense = self.user_info_dict[self.current_user]["Total Expenses"]
        print(f"Your total monthly income: ${self.total_income:,}")
        print(f"Your total monthly expenses: ${self.total_expense:,}")
        self.user_info_dict[self.current_user]["Total Cash Flow"] = self.total_income - self.total_expense
        self.total_cash_flow = self.user_info_dict[self.current_user]["Total Cash Flow"]
        print(f"Your total monthly cash flow is ${self.total_cash_flow:,}")
        sleep(2)
        print("\nReturning to main menu in...")
        sleep(0.5)
        print("3...")
        sleep(1)
        print("2...")
        sleep(1)
        print("1...")
        sleep(1)

    # Add investment type to current user's investment dictionary
    def add_invested(self):
        invested_type = input("Please enter the type of investment: ")
        invested_type = invested_type.title().strip()
        invested_amt = input(f"Please enter the {invested_type} amount: $")
        invested_amt = int(invested_amt.replace(",", ""))
        self.invest_dict[invested_type] = invested_amt
        self.user_info_dict[self.current_user]["Total Investments"] += invested_amt
        print(f"\nYour {invested_type} Investment has been added, {self.current_user}!")

    # Remove investment type from current user's investment dictionary
    def remove_invested(self):
        while True:
            invested_type = input("Which type of investment would you like to remove? ")
            invested_type = invested_type.title().strip()
            if invested_type not in self.invest_dict:
                print(f"\n{invested_type} not found within your investments. Please try again.")
            else:
                print(f"\nYour {invested_type} Investment has been removed, {self.current_user}.")
                self.user_info_dict[self.current_user]["Total Investments"] -= self.invest_dict[invested_type]
                del self.invest_dict[invested_type]
                break

    # Edit investment type in current user's investment dictionary
    def edit_invested(self):
        while True:
            invested_type = input("Which investment type would you like to edit? ")
            invested_type = invested_type.title().strip()
            if invested_type not in self.invest_dict:
                print(f"\n{invested_type} not found within your investments. Please try again.")
            else:
                invested_amt = input(f"Please enter the new {invested_type} amount: $")
                invested_amt = int(invested_amt.replace(",", ""))
                self.user_info_dict[self.current_user]["Total Investments"] -= self.invest_dict[invested_type]
                self.user_info_dict[self.current_user]["Total Investments"] += invested_amt
                self.invest_dict[invested_type] = invested_amt
                print(f"\nYour {invested_type} Investment has been updated!")
                break

    # Show items in current user's invested dictionary and current user's total investment
    def show_invested(self):
        self.total_invest = self.user_info_dict[self.current_user]["Total Investments"]
        print("\nHere is a breakdown of your total investment costs:")
        for invested_type, amount in self.invest_dict.items():
            print(f"\t{invested_type} = ${amount:,}")
        print(f"Total investment costs = ${self.total_invest:,}")
        sleep(2)

    # Investments main menu
    def calc_invested(self):
        while True:
            print("""
            Investment Options:
              [1] Add Investment
              [2] Remove Investment
              [3] Edit Investment
              [4] Show Total Investments
              [5] Return to Main Menu
            """)
            response = input("What would you like to do? ")
            if response == '1':
                self.add_invested()
            elif response == '2':
                self.remove_invested()
            elif response == '3':
                self.edit_invested()
            elif response == '4':
                self.show_invested()
            elif response == '5':
                break
            else:
                print("Invalid input. Please try again.")

    # Calculate current user's Cash on Cash ROI by dividing annual cash flow by total investment
    def calc_cash_ROI(self):
        self.total_cash_flow = self.user_info_dict[self.current_user]["Total Cash Flow"]
        self.total_invest = self.user_info_dict[self.current_user]["Total Investments"]
        self.annual_cash_flow = self.total_cash_flow * 12
        print(f"Your annual cash flow is ${self.annual_cash_flow:,}")
        print(f"Your total investment cost is ${self.total_invest:,}")
        self.cash_ROI = (self.annual_cash_flow/self.total_invest) * 100
        print(f"Your Cash on Cash ROI is {self.cash_ROI}%")
        sleep(2)
        print("\nReturning to main menu in...")
        sleep(0.5)
        print("3...")
        sleep(1)
        print("2...")
        sleep(1)
        print("1...")
        sleep(1)

class Main():

    # Print main menu instructions to user
    def show_instructions():
        print(f"""
        Please select from the following options:
          [1] Calculate Monthly Income
          [2] Calculate Monthly Expenses
          [3] Calculate Monthly Cash Flow
          [4] Calculate Total Investments
          [5] Calculate Cash on Cash ROI
          [6] Add User
          [7] Change User
          [8] Quit
        """)

    # Drives the program
    def run():
        my_ROI = ROI_Calculator()
        
        print("Welcome to Bigger Pockets!\n")
        my_ROI.add_user()

        while True:
            Main.show_instructions()
            response = input(f"What would you like to do, {my_ROI.current_user}? ")
            if response == '1':
                my_ROI.calc_income()
            elif response == '2':
                my_ROI.calc_expenses()
            elif response == '3':
                my_ROI.total_income = my_ROI.user_info_dict[my_ROI.current_user]["Total Income"]
                my_ROI.total_expense = my_ROI.user_info_dict[my_ROI.current_user]["Total Expenses"]
                if my_ROI.total_income and my_ROI.total_expense:
                    my_ROI.calc_cash_flow()
                else:
                    print("\nYou need to add your [1] Monthly Income and [2] Monthly Expenses first before calculating your Monthly Cash Flow.")
            elif response == '4':
                my_ROI.calc_invested()
            elif response == '5':
                my_ROI.total_invest = my_ROI.user_info_dict[my_ROI.current_user]["Total Investments"]
                my_ROI.total_cash_flow = my_ROI.user_info_dict[my_ROI.current_user]["Total Cash Flow"]
                if my_ROI.total_cash_flow and my_ROI.total_invest:
                    my_ROI.calc_cash_ROI()
                else:
                    print("\nYou need to add your [3] Cash Flow and [4] Total Investments first before calculating your Monthly Cash Flow.")
            elif response == '6':
                my_ROI.add_user()
            elif response == '7':
                my_ROI.choose_user()
            elif response == '8':
                print(f"Thank you {my_ROI.current_user} for using the Bigger Pockets ROI Calculator! Have a great day!")
                break
            else:
                print("Invalid input. Please try again.")

Main.run()