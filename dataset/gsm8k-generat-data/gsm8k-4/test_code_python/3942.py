def solution():
    """A firefighter is paid $30 per hour for a 48-hour workweek. He pays 1/3 of the money on rent and $500 on food and $1000 on taxes per month. Calculate the total amount of money the firefighter has after paying his monthly expenses."""
    # Define the firefighter's hourly pay rate and work week
    hourly_pay = 30
    workweek_hours = 48

    # Calculate the firefighter's gross monthly pay
    monthly_gross_pay = hourly_pay * workweek_hours * 4

    # Calculate the firefighter's monthly rent payment
    rent_payment = monthly_gross_pay / 3

    # Define the firefighter's monthly expenses
    food_expenses = 500
    tax_expenses = 1000

    # Calculate the firefighter's total monthly expenses
    total_expenses = rent_payment + food_expenses + tax_expenses

    # Calculate the firefighter's total monthly income after expenses
    monthly_net_income = monthly_gross_pay - total_expenses

    # return the result
    result = monthly_net_income
    return result

print(solution())