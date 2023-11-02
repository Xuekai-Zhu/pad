def solution():
    # Calculate the total hours in a day
    total_hours = 24

    # Calculate the number of hours Jackie spends on work and exercise
    work_and_exercise = 8 + 3

    # Calculate the number of hours Jackie spends on sleep
    sleep_hours = 8

    # Calculate Jackie's free time by subtracting work, exercise and sleep hours from the total hours in a day
    free_time = total_hours - work_and_exercise - sleep_hours

    result = free_time
    return result

print(solution())