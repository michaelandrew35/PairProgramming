class AccountingSystem:
    def __init__(self):
        """
        Initialize the accounting system.
        
        This function sets up the necessary data structures and configurations for the accounting system.
        """
        self.transactions = {}

    def init(self, id):
        """
        Initialize the accounting system.
        
        This function sets up the necessary data structures and configurations for the accounting system.
        """
        print("Initializing accounting system...")
        try:
            with open("input.txt", "r") as file:
                data = file.readlines()
                for line in data:
                    userid, date, expense = line.split()
                    if userid == id:
                        self.transactions.update({date: float(expense)})
                    else:
                        continue
        except FileNotFoundError:
            print("Input file not found. Please ensure 'input.txt' exists.")
        except ValueError:
            print("Error processing input file. Please ensure the format is correct.")
        else:
            if not self.transactions:
                print("No transactions found for user ID:", id)
            else:
                print("Initialization complete. User ID:", id)

    def totalExpenses(self):
        """
        Calculate the total expenses from a list of expenses.
        
        Args:
            expenses (list): A list of expense amounts.
            
        Returns:
            float: The total amount of expenses.
        """
        return sum(self.transactions.values())

    def allTransactions(self):
        """
        Calculate the total amount of all transactions.
        
        Args:
            transactions (list): A list of transaction amounts.
            
        Returns:
            float: The total amount of all transactions.
        """
        for i in self.transactions:
            print(f"Date: {i[:4]}-{i[4:6]}-{i[6:8]}, Amount: {self.transactions[i]}")

    def dayExpenses(self, day):
        """
        Calculate the total expenses for a specific day.
        
        Args:
            expenses (list): A list of tuples where each tuple contains the date and amount of the expense.
            day (str): The date for which to calculate the total expenses in 'YYYY-MM-DD' format.
            
        Returns:
            float: The total amount of expenses for the specified day.
        """
        day = day.replace("-", "")
        if day in self.transactions:
            return self.transactions[day]
        else:
            return -1


    def monthExpenses(self, month):
        """
        Calculate the total expenses for a specific month.
        
        Args:
            expenses (list): A list of tuples where each tuple contains the date and amount of the expense.
            month (str): The month for which to calculate the total expenses in 'YYYY-MM' format.
            
        Returns:
            float: The total amount of expenses for the specified month.
        """
        month = month.replace("-", "")
        expenses = [amount for date, amount in self.transactions.items() if date.startswith(month)]
        return sum(expenses) if expenses else -1

    def exitprogram(self):
        """
        Exit the accounting system.
        
        This function performs any necessary cleanup and exits the program.
        """
        print("Thank you for using the accounting system. Goodbye!")
        exit(0)

user = AccountingSystem()
print("Welcome to the Accounting System")
id = input('Enter your user ID or type "exit" to exit: ')
if id == "exit":
    user.exitprogram()
while not id.isnumeric():
    id = input("Invalid ID. Please enter a valid user ID: ")
user.init(id)
while(1):
    print("""How can we help you?
             1. Total Expenses 
             2. All Transactions
             3. Day Expenses
             4. Month Expenses
             5. Exit""")
    cmd = input("Enter command: ")
    cmd = cmd.strip().lower().replace(" ", "")
    if cmd == "exit" or cmd == "5":
        user.exitprogram()
    elif cmd == "totalexpenses" or cmd == "1":
        print("Total Expenses: ", user.totalExpenses())
    elif cmd == "alltransactions" or cmd == "2":
        print("All Transactions: ")
        user.allTransactions()
    elif cmd == "dayexpenses" or cmd == "3":
        date = input("Enter the date (YYYY-MM-DD): ")
        dayExpenses = user.dayExpenses(date)
        if dayExpenses == -1:
            print(f"No expenses found {date}.")
        else:
            print(f"Day Expenses on {date}: ", dayExpenses) 
    elif cmd == "monthexpenses" or cmd == "4":
        month = input("Enter the month (YYYY-MM): ")
        monthExpenses = user.monthExpenses(month)
        if monthExpenses == -1:
            print(f"No expenses found for {month}.")
        else:
            print(f"Month Expenses on {month}: ", monthExpenses)
    else:
        print("Invalid command")