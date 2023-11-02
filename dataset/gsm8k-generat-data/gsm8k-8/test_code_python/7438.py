def solution():
    # Define Logan's income and expenses
    income = 65000
    rent = 20000
    groceries = 5000
    gas = 8000

    # Calculate Logan's total expenses
    total_expenses = rent + groceries + gas

    # Calculate Logan's remaining income
    remaining_income = income - total_expenses

    # Calculate how much more Logan needs to make each year
    additional_income = 42000 - remaining_income

    result = additional_income
    return result

print(solution())