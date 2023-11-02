def solution():
    """Zilla spent 7% of her monthly earnings on rent, half of it on her other monthly expenses, and put the rest in her savings. If she spent $133 on her rent, how much does she deposit into her savings account in a month?"""
    # Define the percentage of earnings spent on rent
    rent_percentage = 0.07

    # Define the amount spent on rent
    rent_amount = 133

    # Calculate the total monthly earnings
    total_earnings = rent_amount / rent_percentage

    # Calculate the amount spent on other monthly expenses
    expenses_amount = total_earnings / 2

    # Calculate the amount deposited into savings account
    savings_amount = total_earnings - rent_amount - expenses_amount

    result = savings_amount
    return result

print(solution())