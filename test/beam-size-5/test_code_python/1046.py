def solution():
    
    total_distance = 1955
    daily_distance = 325
    num_days = 4
    remaining_distance = total_distance - (daily_distance * num_days)
    result = remaining_distance
    return result

print(solution())