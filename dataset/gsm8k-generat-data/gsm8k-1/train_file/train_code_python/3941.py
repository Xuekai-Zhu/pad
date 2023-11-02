def solution():
    """A firefighter is paid $30 per hour for a 48-hour workweek. He pays 1/3 of the money on rent and $500 on food and $1000 on taxes per month. Calculate the total amount of money the firefighter has after paying his monthly expenses."""
    hourly_rate = 30
    hours_per_week = 48
    weekly_pay = hourly_rate * hours_per_week
    monthly_income = weekly_pay * 4

    rent_portion = monthly_income / 3
    food_expense = 500
    tax_expense = 1000
    total_expenses = rent_portion + food_expense + tax_expense

    total_money_after_expenses = monthly_income - total_expenses
    result = total_money_after_expenses

    return result

print(solution())