def solution():
    hourly_rate = 60
    num_hours_per_day = 8
    num_days = 14
    parts_cost = 2500

    # Calculate the total cost for labor
    labor_cost = hourly_rate * num_hours_per_day * num_days

    # Calculate the total cost for parts and labor
    total_cost = labor_cost + parts_cost
    result = total_cost
    return result

print(solution())