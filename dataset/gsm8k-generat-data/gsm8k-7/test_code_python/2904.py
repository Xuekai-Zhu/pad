def solution():
    part_cost = 20
    labor_cost_per_minute = 0.5
    total_cost = 220

    # Calculate the cost of the two parts
    parts_cost = part_cost * 2

    # Calculate the cost of the labor
    labor_cost = total_cost - parts_cost

    # Calculate the total number of minutes of labor
    total_minutes = labor_cost / labor_cost_per_minute

    # Convert the total minutes to hours
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())