def solution():
    initial_supplies = 400
    first_day_usage = initial_supplies * (2/5)
    second_day_usage = (initial_supplies - first_day_usage) * (3/5)
    remaining_supplies = initial_supplies - first_day_usage - second_day_usage
    result = remaining_supplies
    
    return result

print(solution())