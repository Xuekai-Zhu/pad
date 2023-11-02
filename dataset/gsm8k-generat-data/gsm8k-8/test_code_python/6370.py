def solution():
    # Calculate the total number of hours worked
    total_hours = 8 * 14

    # Calculate the cost of labor
    labor_cost = total_hours * 60

    # Add the cost of parts to the total cost of the repair
    total_cost = labor_cost + 2500

    result = total_cost
    return result

print(solution())