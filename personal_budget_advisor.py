def add_expense(expenses):
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    expenses.append((amount, category))

def add_income(income):
    amount = float(input("Enter income amount: "))
    source = input("Enter source: ")
    income.append((amount, source))

def calculate_totals(expenses, income):
    total_expenses = sum(x[0] for x in expenses)
    total_income = sum(x[0] for x in income)
    savings = total_income - total_expenses
    return total_expenses, total_income, savings

def give_advice(total_expenses, total_income, savings):
    print("\nSummary:")
    print("Total income:", total_income)
    print("Total expenses:", total_expenses)
    print("Savings:", savings)

    if savings < 0:
        print("You are overspending. Try cutting down on non-essential expenses.")
    elif savings < 0.2 * total_income:
        print("Your savings are low. Aim for at least 20% savings.")
    else:
        print("Good job! Your savings rate is healthy.")

def personal_budget_advisor():
    expenses = []
    income = []

    while True:
        choice = input("Enter 'e' to add expense, 'i' to add income, 'q' to quit: ").lower()
        if choice == 'q':
            break
        elif choice == 'e':
            add_expense(expenses)
        elif choice == 'i':
            add_income(income)
        else:
            print("Invalid input. Try again.")

    total_expenses, total_income, savings = calculate_totals(expenses, income)
    give_advice(total_expenses, total_income, savings)

if __name__ == "__main__":
    personal_budget_advisor()
