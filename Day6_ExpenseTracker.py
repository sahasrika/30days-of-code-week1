# Day6_ExpenseTracker.py

import os

FILE = "expenses.txt"

def add_expense():
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")
    with open(FILE, "a") as f:
        f.write(f"{category},{amount},{note}\n")
    print("✅ Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses recorded yet.\n")
        return
    total = 0
    categories = {}
    with open(FILE, "r") as f:
        for line in f:
            category, amount, *_ = line.strip().split(",")
            amount = float(amount)
            total += amount
            categories[category] = categories.get(category, 0) + amount
    print("\n📊 Expense Summary:")
    for c, a in categories.items():
        print(f"{c}: ₹{a}")
    print(f"Total: ₹{total}\n")

while True:
    print("1️⃣ Add Expense")
    print("2️⃣ View Summary")
    print("3️⃣ Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice, try again!\n")
