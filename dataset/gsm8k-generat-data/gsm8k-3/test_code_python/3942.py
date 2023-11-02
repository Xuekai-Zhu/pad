def solution():
    """A firefighter is paid $30 per hour for a 48-hour workweek. He pays 1/3 of the money on rent and $500 on food and $1000 on taxes per month. Calculate the total amount of money the firefighter has after paying his monthly expenses."""
    # Define the firefighter's hourly wage and work hours per week
    HOURLY_WAGE = 30
    WORK_HOURS_PER_WEEK = 48

    # Calculate the firefighter's monthly earnings
    monthly_earnings = HOURLY_WAGE * WORK_HOURS_PER_WEEK * 4

    # Calculate the amount of money the firefighter pays on rent
    rent = monthly_earnings / 3

    # Calculate the total amount of money the firefighter spends on expenses
    total_expenses = rent + 500 + 1000

    # Calculate the total amount of money the firefighter has after paying expenses
    total_money = monthly_earnings - total_expenses

    # Display the total amount of money
    result = total_money
    return result

print(solution())