def solution():
    """Jackie spends 8 hours working, 3 hours of exercise and spends 8 hours of sleep per day. How much free time does Jackie have?"""
    total_hours = 24
    working_hours = 8
    exercise_hours = 3
    sleep_hours = 8
    free_hours = total_hours - working_hours - exercise_hours - sleep_hours
    result = free_hours
    return result

print(solution())