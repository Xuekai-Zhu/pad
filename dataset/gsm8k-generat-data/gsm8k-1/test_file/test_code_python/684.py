def solution():
    """John is very tired. He decides to take a nap, but he wants to finish his homework first. If John has 20 minutes of math homework, 40 minutes of reading homework, and 20 minutes of history homework and 3 hours before he has to eat dinner, how many minutes does John have to nap?"""
    math_homework = 20
    reading_homework = 40
    history_homework = 20
    time_before_dinner = 3*60 # converting hours to minutes
    total_homework_time = math_homework + reading_homework + history_homework
    time_for_nap = time_before_dinner - total_homework_time
    result = time_for_nap
    return result

print(solution())