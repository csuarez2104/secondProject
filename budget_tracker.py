expenses = []
expense1 = {'amount': '51.00', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'amount': '21.00', 'category': 'food'}
expenses.append(expense2)

def removeExpense():
    while  True:
        listExpenses()
        print("What expense would you like to take off.")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except:
            print("Invalid input.")

def addExpense(amount, category):
    expense = {'amount': amount,'category': category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options")
    print("1. Add a new expense.")
    print("2. Remove an expense.")
    print("3. List all expenses.")

def listExpenses():
    print("/n Here is a list of your expenses...")
    print("----------------------------")
    counter = 0
    for expense in expenses:
        print("#", counter," - ", expense['amount'], " - ", expense['category'])
        counter += 1
    print("/n /n")

if __name__ == "__main__":
    while True:
        ### Promp the user
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            print("How much was this expense?")
            while True:
                try:
                    amountToadd = input("> ")
                    break
                except:
                    print("Invalid input.")

            print("What category was this expense?")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                    print("Invalid input.")

            addExpense(amountToadd, category)
        elif optionSelected == "2":
            removeExpense()
        elif optionSelected == "3":
            listExpenses()
        else:
            print("Invalid input.")
