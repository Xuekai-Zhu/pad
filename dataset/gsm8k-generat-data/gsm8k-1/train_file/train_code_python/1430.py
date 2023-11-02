def solution():
    """Tony is driving his car between his town and a friend's down. The towns are 120 miles apart and he gets there in 3 hours. The next day, he is driving to see another friend who lives 200 miles away from his friend. If he drives at the same speed, how long will the drive take?"""
    distance_1 = 120
    time_1 = 3
    speed_1 = distance_1 / time_1
    distance_2 = 200
    time_2 = distance_2 / speed_1
    result = time_2
    return result

print(solution())