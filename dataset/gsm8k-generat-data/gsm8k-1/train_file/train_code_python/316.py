def solution():
    """Madeline spends 18 hours a week in class. She spends 4 hours per day working on homework. She spends 8 hours per day sleeping. She works part-time 20 hours per week. How many hours left over does Madeline have?"""
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