def solution():
    # Calculate the total time Janice needs to finish her tasks
    homework_time = 30  # in minutes
    cleaning_time = homework_time / 2  # in minutes
    dog_walk_time = homework_time + 5  # in minutes
    trash_time = homework_time / 6  # in minutes
    total_time = homework_time + cleaning_time + dog_walk_time + trash_time  # in minutes

    # Calculate the time left before the movie starts
    time_left = (2 * 60) - total_time  # in minutes
    result = time_left
    return result

print(solution())