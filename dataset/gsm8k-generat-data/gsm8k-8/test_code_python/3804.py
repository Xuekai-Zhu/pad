def solution():
    current_hours = 4
    recommended_hours = 6
    sleep_deficit_per_day = recommended_hours - current_hours
    sleep_deficit_per_week = sleep_deficit_per_day * 7
    result = sleep_deficit_per_week
    return result

print(solution())