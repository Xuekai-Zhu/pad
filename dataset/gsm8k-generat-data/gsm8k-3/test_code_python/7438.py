def solution():
    """Logan makes $65,000 a year. He spends $20,000 on rent every year, $5000 on groceries every year, and $8000 on gas every year. If he wants to have at least $42000 left, how much more money must he make each year?"""
    # Define Logan's income and expenses
    income = 65000
    rent = 20000
    groceries = 5000
    gas = 8000

    # Calculate Logan's total expenses
    total_expenses = rent + groceries + gas

    # Calculate Logan's desired savings
    desired_savings = 42000

    # Calculate the minimum amount Logan needs to make each year to meet his savings goal
    min_income = total_expenses + desired_savings

    # Calculate how much more Logan needs to make each year
    more_income = min_income - income

    # Display how much more Logan needs to make each year
    result = more_income
    return result

print(solution())