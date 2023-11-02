def solution():
    """Bob drove for one and a half hours at 60/mph. He then hit construction and drove for 2 hours at 45/mph. How many miles did Bob travel in those 3 and a half hours?"""
    speed1 = 60
    time1 = 1.5
    distance1 = speed1 * time1
    speed2 = 45
    time2 = 2
    distance2 = speed2 * time2
    total_distance = distance1 + distance2
    result = total_distance
    return result

print(solution())