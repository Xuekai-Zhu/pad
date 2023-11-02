def solution():
    """Jace drives 60 miles per hour. If Jace drives for 4 hours straight, takes a 30-minute break, and then drives for another 9 hours straight, how many miles will he travel?"""
    speed = 60
    time_1 = 4
    time_2 = 9
    break_time = 0.5 # in hours
    distance_1 = speed * time_1
    distance_2 = speed * time_2
    total_distance = distance_1 + distance_2
    total_time = time_1 + break_time + time_2
    result = total_distance
    return result

print(solution())