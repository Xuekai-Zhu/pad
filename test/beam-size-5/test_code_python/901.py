def solution():
    
    sleep_hours_per_night = 10
    dog_hours_per_day = sleep_hours_per_night - 2
    total_sleep_hours_per_day = sleep_hours_per_night + dog_hours_per_day
    free_hours_per_day = total_sleep_hours_per_day - 10
    result = free_hours_per_day
    return result

print(solution())