def solution():
    """Zilla spent 7% of her monthly earnings on rent, half of it on her other monthly expenses, and put the rest in her savings. If she spent $133 on her rent, how much does she deposit into her savings account in a month?"""
    # Define the percentage of monthly earnings spent on rent
    RENT_PERCENTAGE = 0.07

    # Define the amount spent on rent
    rent = 133

    # Calculate the total monthly earnings
    total_earnings = rent / RENT_PERCENTAGE

    # Calculate the amount spent on other monthly expenses
    other_expenses = total_earnings / 2

    # Calculate the amount deposited into savings
    savings = total_earnings - rent - other_expenses

    # Display the amount deposited into savings
    result = savings
    return result

print(solution())