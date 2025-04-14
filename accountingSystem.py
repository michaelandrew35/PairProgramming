class AccountingSystem:
    """ A class to represent an accounting system. """

    def __init__(self):
        """Initialize the accounting system, by setting up the necessary data structures and configurations for the accounting system.

        :param : None
        :type : None
        :returns: None
        :rtype: None

        Running Example: user = AccountingSystem(); initializes the accounting system with an empty list of transactions.
        """
        self.transactions = []

    def init(self, id):
        """ Read the input file and initialize the accounting system with user data according to their id.

        :param id: The user ID to initialize the accounting system with.
        :type id: str
        :returns: None
        :rtype: None

        Running Example: user.init('15317546'); reads the input file and initializes the transactions for user with id '15317546'
        """
        with open("input.txt", "r") as file:
            data = file.readlines()
            for line in data:
                userid, date, expense = line.split()
                if userid == id:
                    self.transactions.append((date, float(expense)))
        if not self.transactions:
            print("No transactions found for user ID:", id)
        else:
            print("Initialization complete. User ID:", id)

    def totalExpenses(self):
        """ Calculate the total expenses from a list of expenses.

        :param : None
        :type : None
        :returns: the total expenses of the user.
        :rtype: float

        Running Example: user.totalExpenses(); returns 150.0 for user with id '15317546'
        """
        return sum(amount for _, amount in self.transactions)

    def allTransactions(self):
        """ Display the transaction dates and amounts for the user.

        :param : None
        :type : None
        :returns: None
        :rtype: None

        Running Example: user.allTransactions(); prints all transactions for user with id '15317546'
        """
        for date, amount in self.transactions:
            print(
                f"Date: {date[:4]}-{date[4:6]}-{date[6:8]}, Amount: {amount}")

    def dayExpenses(self, day):
        """ Calculate the total expenses for a specific day.

        :param day: The date for which to calculate the total expenses in 'YYYY-MM-DD' format.
        :type day: str
        :returns: the total expenses for the specified day if any transactions exist.
        :rtype: float

        Running Example: user.dayExpenses('2023-03-01'); returns 150.0 for user with id '15317546'
        """
        day = day.replace("-", "")
        daily = [amount for date, amount in self.transactions if date == day]
        if not daily:
            return -1
        return sum(daily)

    def monthExpenses(self, month):
        """ Calculate the total expenses for a specific month.

        :param month: The month for which to calculate the total expenses in 'YYYY-MM' format.
        :type month: str
        :returns: the average expenses for the specified month if any transactions exist.
        :rtype: float

        Running Example: user.monthExpenses('2023-03'); returns 4.838709677419355 for user with id '15317546'
        """
        month = month.replace("-", "")
        monthly = [amount for date,
                   amount in self.transactions if date.startswith(month)]
        datenum = 30 if month[4:6] in ["04", "06", "09", "11"] else 31
        if month[4:6] == "02":
            year = int(month[:4])
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                datenum = 29
            else:
                datenum = 28
        if int(month[4:6]) <= 0 or int(month[4:6]) > 12:
            return -1
        if not monthly:
            return -1
        return sum(monthly) / datenum

    def exitprogram(self):
        """Exit the accounting system.

        :param : None
        :type : None
        :returns: None
        :rtype: None

        Running Example: user.exitprogram(); exits the accounting system and prints a goodbye message.
        """
        print("Thank you for using the accounting system. Goodbye!")
        exit(0)


if __name__ == "__main__":
    user = AccountingSystem()
    print("Welcome to the Accounting System")
    id = input('Enter your user ID or type "exit" to exit: ')
    if id == "exit":
        user.exitprogram()
    while not id.isnumeric():
        id = input("Invalid ID. Please enter a valid user ID: ")
    user.init(id)
    while True:
        print("""How can we help you?
                 1. Total Expenses 
                 2. All Transactions
                 3. Day Expenses
                 4. Month Expenses
                 5. Exit""")
        cmd = input("Enter command: ").strip().lower().replace(" ", "")
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
