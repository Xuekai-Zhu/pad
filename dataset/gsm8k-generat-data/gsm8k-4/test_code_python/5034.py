def solution():
    """Jackie spends 8 hours working, 3 hours of exercise and spends 8 hours of sleep per day. How much free time does Jackie have?"""
    # Define the total number of hours in a day
    total_hours = 24

    # Calculate the total time Jackie spends on work, exercise, and sleep
    work_hours = 8
    exercise_hours = 3
    sleep_hours = 8

    # Calculate the amount of free time Jackie has
    free_hours = total_hours - work_hours - exercise_hours - sleep_hours

    result = free_hours
    return result

print(solution())