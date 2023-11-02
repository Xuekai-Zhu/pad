def solution():
    """Jackie spends 8 hours working, 3 hours of exercise and spends 8 hours of sleep per day. How much free time does Jackie have?"""
    # Define the total number of hours in a day
    TOTAL_HOURS = 24

    # Calculate the total number of hours spent on work, exercise, and sleep
    work_hours = 8
    exercise_hours = 3
    sleep_hours = 8

    # Calculate the total number of hours spent on non-free time activities
    non_free_hours = work_hours + exercise_hours + sleep_hours

    # Calculate the number of free hours
    free_hours = TOTAL_HOURS - non_free_hours

    # Display the number of free hours
    result = free_hours
    return result

print(solution())