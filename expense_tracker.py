# EXPENSE TRACKER
# FUNCTIONS NEEDED TO:
# SAVE & LOAD
# ADD NEW EXPENSES (AMOUNT, CATEGORY ETC)
# SUMMARY OF TOTAL
# DATE SO DAILY/WEEKLY/MONTHLY/YEARLY EXPENSES CAN BE CALCULATED

import json 
import os

# INIT MESSAGE
def message():
    print("******* Expense Tracker *******")


# LOAD JSON
def load_expenses(filename="expenses.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error loading data. File may be corrupt. Starting new file.")
                return []
    return []

# SAVE JSON
def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

# EXPENSE INPUT FUNCTION
# ERROR HANDLING NEEDED
def get_expense_amount():
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Amount must be a positive number. Try again.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Enter a valid number.")

# EXPENSE CATEGORY FUNCTION
# ADD ERROR HANDLING
def get_expense_category():
    categories = ["Food", "Transport", "Entertainment", "Utilities", "Holidays", "Savings", "Other"]
    while True:
        print("\nSelect an expense category from the following:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Invalid choice. Select a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

# EXPENSE DESCRIPTION FUNCTION
def get_expense_description():
    description = input("Enter a description for the expense: ")
    return description

# LIST FUNCTION
def store_expense(expenses, amount, category, description):
    expense = {
        "Amount": amount,
        "Category": category,
        "Description": description
    }
    expenses.append(expense)

# DISPLAY SUMMARY FUNCTION
def display_summary(expenses):
    if not expenses:
        print("No expenses logged.")
        return
    
    total_spent = sum(expense["Amount"] for expense in expenses)
    print("\n*******Expense Summary*******")
    print(f"Total amount spent: ${total_spent:.2f}")
    
    category_totals = {}
    for expense in expenses:
        category = expense["Category"]
        if category in category_totals:
            category_totals[category] += expense["Amount"]
        else:
            category_totals[category] = expense["Amount"]
    
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
    
    print("\n*******All Expenses*******")
    for expense in expenses:
        print(f"Amount: ${expense['Amount']:.2f}, Category: {expense['Category']}, Description: {expense['Description']}")

# MAIN - LOAD EXPENSES - DISPLAY OPTIONS - USER INPUT CHOICE(LOG EXPENSE, SUMMARY, EXIT) - SAVE BEFORE EXITING
# ADD ERROR HANDLING
def main():
    filename = "expenses.json"
    expenses = load_expenses(filename)
    message()
    
    while True:
        print("\nOptions:")
        print("1. Log Expense")
        print("2. View Summary")
        print("3. Exit")
        
        try:
            choice = int(input("Select an option (1-3): "))
            if choice == 1:
                amount = get_expense_amount()
                category = get_expense_category()
                description = get_expense_description()
                store_expense(expenses, amount, category, description)
                save_expenses(expenses, filename)
                print("**Expense logged.**")
            elif choice == 2:
                display_summary(expenses)
            elif choice == 3:
                print("**Closing Expense Tracker.**")
                save_expenses(expenses, filename)
                break
            else:
                print("Invalid option. Select between 1 and 3.")
        except ValueError:
            print("Invalid input. Enter a valid option.")

if __name__ == "__main__":
    main()

    