def solution():
    time_needed = 30
    time_available = 2:30
    time_used_by_oldest_daughter = 45
    time_used_by_youngest_daughter = 30
    time_used_by_husband = 20
    time_left = time_available - time_used_by_oldest_daughter - time_used_by_youngest_daughter - time_used_by_husband
    result = time_left
    return result

print(solution())