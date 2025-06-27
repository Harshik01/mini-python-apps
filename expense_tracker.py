expenses = []
while True:
    print (f"\n💸 Expense Tracker")
    print(f"1. Add an expense")
    print(f"2. View all expenses")
    print(f"3. Exit")
    choice = int(input(f"Enter your choice: "))
    if choice == 3:
        break
    elif choice == 1:
        amount = float(input("Enter amount: "))
        reason = input("What it is for: ")
        expenses.append((amount, reason))
        print("✅ Expense added!")
    else:
        if len(expenses) == 0:
            print("No expenses found")
        else:
            for index, expense in enumerate(expenses, start=1):
                amount, reason = expense
                print(f"{index}. {expense}")