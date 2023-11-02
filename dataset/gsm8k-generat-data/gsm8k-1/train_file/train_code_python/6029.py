def solution():
    """A car driving cross-country traveled 180 miles in 4 hours. At this rate of speed, how many miles further will the car travel in the next 3 hours?"""
    distance = 180
    time = 4
    speed = distance / time
    additional_time = 3
    additional_distance = speed * additional_time
    result = additional_distance
    return result

print(solution())