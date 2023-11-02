def solution():
    homework_time = 30
    room_cleaning_time = homework_time / 2
    dog_walking_time = homework_time + 5
    trash_time = homework_time / 6
    total_time = homework_time + room_cleaning_time + dog_walking_time + trash_time
    remaining_time = (2 * 60) - total_time
    result = remaining_time
    return result

print(solution())