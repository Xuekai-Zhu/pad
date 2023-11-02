def solution():
    """If Jade earns $1600 per month and spent 75% of it on living expenses, one-fifth on insurance, and saves the rest, how much does she save per month?"""
    # Define Jade's monthly earnings
    earnings = 1600

    # Calculate Jade's living expenses
    living_expenses = earnings * 0.75

    # Calculate Jade's insurance payments
    insurance_payments = earnings * (1/5)

    # Calculate Jade's savings
    savings = earnings - living_expenses - insurance_payments

    # Display Jade's monthly savings
    result = savings
    return result

print(solution())