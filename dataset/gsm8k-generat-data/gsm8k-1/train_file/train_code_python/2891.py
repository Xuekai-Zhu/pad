def solution():
    """John travels 150 miles in 2 hours. The speed limit is 60 mph. How many mph above the speed limit was he driving?"""
    distance = 150
    time = 2
    speed = distance / time
    speed_limit = 60
    mph_above_speed_limit = speed - speed_limit
    result = mph_above_speed_limit
    return result

print(solution())