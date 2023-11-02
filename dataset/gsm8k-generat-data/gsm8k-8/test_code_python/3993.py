def solution():
    # Calculate utilities cost based on 20% of rent
    utilities_cost = 0.2 * 1200

    # Calculate total employee cost per shift
    employee_cost_per_shift = 2 * 12.50 * 8

    # Calculate total employee cost for 5 days
    employee_cost_per_week = employee_cost_per_shift * 5

    # Calculate total weekly expenses
    total_expenses = 1200 + utilities_cost + employee_cost_per_week
    result = total_expenses
    return result

print(solution())