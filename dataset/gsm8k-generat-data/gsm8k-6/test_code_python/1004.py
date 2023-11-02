def solution():
    # Calculate the total number of hours worked by both professionals
    total_hours = 6 * 7 * 2  # 6 hours a day, 7 days a week, with 2 professionals

    # Calculate the total cost for hiring the professionals
    cost_per_hour = 15  # one of the professionals is paid $15/hr
    total_cost = total_hours * cost_per_hour

    result = total_cost
    return result

print(solution())