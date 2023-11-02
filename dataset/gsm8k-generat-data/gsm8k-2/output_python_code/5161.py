def solution():
    """A train travels 360 miles in 3 hours. At the same rate, how many additional hours would it take to travel an additional 240 miles?"""
    distance_1 = 360
    time_1 = 3
    speed = distance_1 / time_1
    distance_2 = 240
    time_2 = distance_2 / speed
    result = time_2 - time_1
    return result

print(solution())