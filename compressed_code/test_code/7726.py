def solution():
    
    towels_per_wash = 7
    wash_time = 1
    total_wash_time = 2
    num_towels = 98
    num_washes = num_towels / towels_per_wash
    time_per_wash = wash_time
    total_time = num_washes * time_per_wash
    num_days = total_time / total_wash_time
    result = num_days
    return result

print(solution())