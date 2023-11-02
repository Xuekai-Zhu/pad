def solution():
    """A firefighter is paid $30 per hour for a 48-hour workweek. He pays 1/3 of the money on rent and $500 on food and $1000 on taxes per month. Calculate the total amount of money the firefighter has after paying his monthly expenses."""
    hourly_wage = 30
    weekly_hours = 48
    monthly_wage = hourly_wage * weekly_hours * 4
    rent = monthly_wage / 3
    food = 500
    taxes = 1000
    total_expenses = rent + food + taxes
    remaining_money = monthly_wage - total_expenses
    result = remaining_money
    return result

print(solution())