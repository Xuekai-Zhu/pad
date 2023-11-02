def solution():
    """To make 3 km, Ben walked for 2 hours. Continuing at the same speed, how much time in minutes would it take him to travel 12 km?"""
    distance_1 = 3
    time_1 = 120
    speed = distance_1 / time_1
    distance_2 = 12
    time_2 = distance_2 / speed * 60
    result = time_2
    return result

print(solution())