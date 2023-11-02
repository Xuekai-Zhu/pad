def solution():
    rent = 1200
    utilities_percent = 0.2
    num_employees_per_shift = 2
    hours_per_day = 16
    num_days = 5
    employee_pay_per_hour = 12.5

    # Calculate the cost of utilities
    utilities_cost = rent * utilities_percent

    # Calculate the total number of employee hours per week
    total_employee_hours = num_employees_per_shift * hours_per_day * num_days

    # Calculate the total employee pay per week
    total_employee_pay = total_employee_hours * employee_pay_per_hour

    # Calculate the total weekly expenses
    total_expenses = rent + utilities_cost + total_employee_pay
    result = total_expenses
    return result

print(solution())