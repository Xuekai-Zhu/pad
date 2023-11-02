def solution():
    total_time = 120 # in minutes
    homework_time = 30
    room_cleaning_time = homework_time / 2
    dog_walking_time = homework_time + 5
    trash_time = homework_time / 6

    # calculate total time spent on tasks
    total_time_spent = homework_time + room_cleaning_time + dog_walking_time + trash_time

    remaining_time = total_time - total_time_spent
    result = remaining_time
    return result

print(solution())