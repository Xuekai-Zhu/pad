def solution():
    """If Jade earns $1600 per month and spent 75% of it on living expenses, one-fifth on insurance, and saves the rest, how much does she save per month?"""
    # Define Jade's monthly income
    income = 1600

    # Calculate the amount spent on living expenses
    living_expenses = income * 0.75

    # Calculate the amount spent on insurance
    insurance = income * (1/5)

    # Calculate the amount saved
    savings = income - living_expenses - insurance

    # return the result
    result = savings
    return result

print(solution())