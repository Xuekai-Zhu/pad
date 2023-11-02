def solution():
    hours_working = 8
    hours_exercising = 3
    hours_sleeping = 8
    total_hours = hours_working + hours_exercising + hours_sleeping
    free_time = 24 - total_hours
    result = free_time
    return result

print(solution())