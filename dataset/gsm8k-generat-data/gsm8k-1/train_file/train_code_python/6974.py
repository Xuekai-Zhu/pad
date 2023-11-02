def solution():
    """To make 3 km, Ben walked for 2 hours. Continuing at the same speed, how much time in minutes would it take him to travel 12 km?"""
    distance1 = 3
    time1 = 2
    speed = distance1 / time1  # km/hour
    distance2 = 12
    time2 = distance2 / speed  # hours
    time2_minutes = time2 * 60  # convert to minutes
    result = time2_minutes
    return result

print(solution())