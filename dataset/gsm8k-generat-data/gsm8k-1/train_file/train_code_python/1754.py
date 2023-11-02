def solution():
    """John gets lost on his way home. His normal trip is 150 miles and would take him 3 hours. He ends up driving 50 miles out of the way and has to get back on track. How long did the trip take if he kept the same speed?"""
    normal_distance = 150
    added_distance = 50
    total_distance = normal_distance + added_distance
    normal_time = 3
    speed = normal_distance / normal_time
    extra_time = added_distance / speed
    total_time = normal_time + extra_time
    result = total_time
    return result

print(solution())