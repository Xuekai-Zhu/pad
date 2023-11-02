def solution():
    """A train travels 270 miles in 3 hours. At the same rate, how many additional hours would it take to travel an additional 180 miles?"""
    distance_1 = 270
    time_1 = 3
    distance_2 = 180
    rate = distance_1/time_1
    time_2 = distance_2/rate
    result = time_2 - time_1
    return result

print(solution())