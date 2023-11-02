def solution():
    """Janice needs to go to watch a movie in 2 hours. before she could leave, she needs to finish her homework which takes 30 minutes; clean her room which takes half as long as her homework; walk the dog which takes 5 minutes more than making homework; take out the trash which takes 1/6 of the time it takes her to do the homework. How many more minutes do Janice have left before the movie starts?"""
    homework_time = 30
    room_cleaning_time = homework_time / 2
    dog_walking_time = homework_time + 5
    trash_time = homework_time / 6
    total_time = homework_time + room_cleaning_time + dog_walking_time + trash_time
    time_left = (2 * 60) - total_time
    result = time_left
    return result

print(solution())