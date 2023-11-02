def solution():
    hours_worked = 8 * 14  # The mechanic works 8 hours a day for 14 days
    hourly_rate = 60  # The mechanic charges $60 per hour
    parts_cost = 2500  # The mechanic used $2500 in parts

    # Calculate the total cost of labor
    labor_cost = hours_worked * hourly_rate

    # Calculate the total cost of repairs
    total_cost = labor_cost + parts_cost
    result = total_cost
    return result

print(solution())