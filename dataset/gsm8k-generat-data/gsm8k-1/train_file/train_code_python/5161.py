def solution():
    """A train travels 360 miles in 3 hours. At the same rate, how many additional hours would it take to travel an additional 240 miles?"""
    distance = 360
    time = 3
    speed = distance / time
    additional_distance = 240
    additional_time = additional_distance / speed
    result = additional_time
    return result

print(solution())