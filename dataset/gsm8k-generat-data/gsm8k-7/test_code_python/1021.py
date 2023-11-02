def solution():
    total_time = 3*60   # convert 3 hours to minutes

    math_time = 45
    english_time = 30
    science_time = 50
    history_time = 25

    # Calculate the total time spent on all homework
    total_homework_time = math_time + english_time + science_time + history_time

    # Calculate the time left for the special project
    time_left = total_time - total_homework_time

    result = time_left
    return result

print(solution())