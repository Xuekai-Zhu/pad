def solution():
    total_time = 2 * 60  # convert 2 hours to minutes
    piano_time = 30
    writing_time = 25
    history_time = 38

    # Calculate the total time spent on music practice
    total_practice_time = piano_time + writing_time + history_time

    # Calculate the time left for using the finger exerciser
    time_left = total_time - total_practice_time
    result = time_left
    return result

print(solution())