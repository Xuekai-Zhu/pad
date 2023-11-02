def solution():
    """James opens up a flower shop.  He needs to pay rent of $1200 a week with an additional 20% of rent to pay for utilities and he has 2 employees per shift with the store open 16 hours a day for 5 days a week.  If he pays each employee $12.50 an hour, what are his weekly expenses to run the store?"""
    # Define the rent and utilities cost
    RENT_COST = 1200
    UTILITIES_MULTIPLIER = 0.2

    # Calculate the utilities cost
    utilities_cost = RENT_COST * UTILITIES_MULTIPLIER

    # Define the number of employees and hours worked
    employees_per_shift = 2
    hours_per_day = 16
    days_per_week = 5

    # Calculate the total number of employee hours worked per week
    employee_hours_per_week = employees_per_shift * hours_per_day * days_per_week

    # Define the employee hourly wage
    hourly_wage = 12.5

    # Calculate the total employee wage cost per week
    employee_wage_cost_per_week = employee_hours_per_week * hourly_wage

    # Calculate the total weekly expenses
    total_expenses = RENT_COST + utilities_cost + employee_wage_cost_per_week

    # Display the total weekly expenses
    result = total_expenses
    return result

print(solution())