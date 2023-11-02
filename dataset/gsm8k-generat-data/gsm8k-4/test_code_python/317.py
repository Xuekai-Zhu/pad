def solution():
    """Madeline spends 18 hours a week in class. She spends 4 hours per day working on homework. She spends 8 hours per day sleeping. She works part-time 20 hours per week. How many hours left over does Madeline have?"""
    # Define the amount of time spent on homework and sleeping each week
    homework_time = 4 * 7
    sleep_time = 8 * 7

    # Define the total amount of time Madeline spends in class and working each week
    class_time = 18
    work_time = 20

    # Calculate the total amount of time Madeline spends each week
    total_time = homework_time + sleep_time + class_time + work_time

    # Calculate the amount of time left over
    leftover_time = 168 - total_time

    # Return the result
    result = leftover_time
    return result

print(solution())