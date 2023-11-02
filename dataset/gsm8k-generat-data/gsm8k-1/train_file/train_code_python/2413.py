def solution():
    """If Amanda can run the length of a football field 2000 meters in length in 2 hours, how long would it take her to run the length of a 10000-meter track at the same speed?"""
    distance1 = 2000
    time1 = 2
    speed = distance1 / time1
    distance2 = 10000
    time2 = distance2 / speed
    result = time2
    return result

print(solution())