def solution():
    """Mason is on his bike journey at a rate of 8 miles per hour. He travels for 4 hours, takes some rest, and then goes on for another 6 hours. How many miles has he traveled in total?"""
    speed = 8
    time1 = 4
    time2 = 6
    distance = speed * (time1 + time2)
    result = distance
    return result

print(solution())