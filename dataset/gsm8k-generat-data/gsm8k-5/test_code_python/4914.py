def solution():
    time_for_homework = 30
    time_for_cleaning = time_for_homework / 2
    time_for_dog_walking = time_for_homework + 5
    time_for_trash = time_for_homework / 6
    total_time = time_for_homework + time_for_cleaning + time_for_dog_walking + time_for_trash
    time_left = (2 * 60) - total_time
    result = time_left
    return result

print(solution())