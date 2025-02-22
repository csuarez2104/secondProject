from expenses import Expense
import datetime
import calendar

def main():
    print("Welcome to the Budget Tracker!")
    budget = 2000
    expense_file_path = "expenses.csv"


    #Remove an expense.
    remove_expense(expense_file_path)

    # Get user input for expense.
    expense = get_expense()

    # Write their expense to a file.
    save_expense_file(expense, expense_file_path)

    


    #read file and summarize expenses.
    summarize_expense(expense_file_path, budget )
    

def get_expense():

    expense_name= input("Enter the expense name: ")
    expense_amount = float(input("Enter the amount: "))
    

    expense_category = ["Food", "Rent", "Work", "Fun","Subscriptions"]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f" {i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Enter a category number{value_range}:")) - 1


        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name=expense_name, amount=expense_amount, category=selected_category)

            return new_expense
        else:
            print("Invalid category number. Please try again.")
   


def save_expense_file(expense: Expense, expense_file_path):
    print("Saving User expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a")as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def remove_expense(expense_file_path):
    remove_question = input("Do you want to remove an expense? (y/n): ")
    if remove_question == "y":
        expense_name = input("Enter the expense name to remove: ")

        with open(expense_file_path, "r") as f:
            lines = f.readlines()
    
        with open(expense_file_path, "w") as f:
            for line in lines:
                if expense_name not in line:
                    f.write(line)
        print(f"Removed {expense_name} from expenses")
    else:
        pass
 

def summarize_expense(expense_file_path, budget):
    print("Summarizing expenses")
    expenses : list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line_elements = line.strip().split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)
    

    amount_by_category = {}
    for expense in expenses:
       key = expense.category
       if key in amount_by_category:
            amount_by_category[key] += expense.amount
       else:
            amount_by_category[key] = expense.amount 
    
    
    print("Expenses by category:")
    for key, amount in amount_by_category.items():
        print(f"{key}: ${amount:.2f}")
    
    total_spent = sum(expense.amount for expense in expenses)
    print(f"Total spent: ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    if remaining_budget > 0:
        print(f"Remaining Budget: ${remaining_budget:.2f}")
    else:
        print(f"Over Budget by ${remaining_budget:.2f}")

    now = datetime.datetime.now()

    days_in_month = calendar.monthrange(now.year, now.month)[1]

    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"Daily Budget: ${daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"   




 

if __name__ == "__main__":
    main()