from expense_manager import add_expense, view_expenses, total_by_category

def show_menu():
    print("\n===== 💰 Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expense by Category")
    print("4. Exit")
    return input("Choose an option: ")

def main():
    while True:
        choice = show_menu()

        if choice == "1":
            category = input("Enter category (Food/Travel/Shopping/etc): ").capitalize()
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            add_expense(category, amount, description)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_by_category()

        elif choice == "4":
            print("👋 Exiting... Your data is saved safely.")
            break

        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
