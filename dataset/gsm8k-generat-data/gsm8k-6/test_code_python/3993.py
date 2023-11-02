def solution():
    # Calculate the total number of employees per week
    employees_per_shift = 2
    shifts_per_day = 2
    hours_per_day = 16
    days_per_week = 5
    total_employees = employees_per_shift * shifts_per_day * hours_per_day * days_per_week

    # Calculate the total cost of employees per week
    hourly_rate = 12.50
    total_employee_cost = hourly_rate * total_employees

    # Calculate the total cost of rent and utilities per week
    rent = 1200
    utilities = 0.2 * rent
    total_rent_cost = rent + utilities

    # Calculate the total weekly expenses for the flower shop
    total_expenses = total_employee_cost + total_rent_cost
    result = total_expenses
    return result

print(solution())