def solution():
    
    class_hours_per_week = 18
    homework_hours_per_day = 4
    sleep_hours_per_day = 8
    part_time_hours_per_week = 20
    total_hours_per_week = 24*7
    hours_spent_per_week = class_hours_per_week + (homework_hours_per_day * 7) + (sleep_hours_per_day * 7) + part_time_hours_per_week
    hours_left_over = total_hours_per_week - hours_spent_per_week
    result = hours_left_over
    return result

print(solution())