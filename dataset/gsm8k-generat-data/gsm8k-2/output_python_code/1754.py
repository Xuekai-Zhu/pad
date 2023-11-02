def solution():
    """John gets lost on his way home. His normal trip is 150 miles and would take him 3 hours. He ends up driving 50 miles out of the way and has to get back on track. How long did the trip take if he kept the same speed?"""
    normal_speed = 50  # miles per hour
    normal_distance = 150  # miles
    normal_time = normal_distance / normal_speed  # hours
    extra_distance = 50  # miles
    total_distance = normal_distance + extra_distance  # miles
    total_time = normal_time + (extra_distance / normal_speed)  # hours
    result = total_time
    return result

print(solution())