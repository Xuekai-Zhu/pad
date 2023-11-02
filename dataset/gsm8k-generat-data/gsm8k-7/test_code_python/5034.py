def solution():
    total_hours = 24
    work_hours = 8
    exercise_hours = 3
    sleep_hours = 8

    # Calculate the total amount of time spent on work, exercise, and sleep
    total_busy_hours = work_hours + exercise_hours + sleep_hours

    # Calculate the total free time
    free_time = total_hours - total_busy_hours
    result = free_time
    return result

print(solution())