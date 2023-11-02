def solution():
    hours_per_day = 6
    num_days = 7
    hourly_rate = 15

    # Calculate the total hours worked by both professionals
    total_hours_worked = 2 * hours_per_day * num_days

    # Calculate the total cost of hiring the professionals
    total_cost = total_hours_worked * hourly_rate
    result = total_cost
    return result

print(solution())