def solution():
    # Calculate the cost of labor
    labor_cost = 220 - (20 * 2)  # Total cost - cost of parts
    # Calculate the number of minutes of labor
    labor_minutes = labor_cost / 0.5
    # Convert minutes to hours
    labor_hours = labor_minutes / 60
    result = labor_hours
    return result

print(solution())