import csv
import os


FILE_NAME = "expenses.csv"


def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("Expense added successfully.")


def view_expenses():
    print("\n--- All Expenses ---")

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            found = True
            print(
                row["Date"],
                "|",
                row["Category"],
                "|",
                row["Description"],
                "| ₹",
                row["Amount"]
            )

        if not found:
            print("No expenses found.")


def filter_expenses():
    print("\n--- Filter Expenses ---")

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    category = input("Enter category to filter: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            if row["Category"].lower() == category:
                found = True
                print(
                    row["Date"],
                    "|",
                    row["Category"],
                    "|",
                    row["Description"],
                    "| ₹",
                    row["Amount"]
                )

        if not found:
            print("No expenses found for this category.")


def category_summary():
    print("\n--- Category Summary ---")

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    totals = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    if not totals:
        print("No expenses found.")
        return

    for category, total in totals.items():
        print(category, ": ₹", total)


while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        filter_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")