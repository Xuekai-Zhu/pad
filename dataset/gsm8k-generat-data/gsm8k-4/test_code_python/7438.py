def solution():
    """Logan makes $65,000 a year. He spends $20,000 on rent every year, $5000 on groceries every year, and $8000 on gas every year. If he wants to have at least $42000 left, how much more money must he make each year?"""
    # Define Logan's income and expenses
    income = 65000
    rent = 20000
    groceries = 5000
    gas = 8000

    # Calculate Logan's total expenses
    total_expenses = rent + groceries + gas

    # Calculate the amount Logan wants to have left
    desired_leftover = 42000

    # Calculate the amount Logan currently has left
    current_leftover = income - total_expenses

    # Calculate the additional amount Logan needs to make to reach his desired leftover
    additional_income = desired_leftover - current_leftover

    result = additional_income
    return result

print(solution())