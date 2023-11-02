def solution():
    """Chrystal’s vehicle speed is 30 miles per hour. Ascending the mountain decreases its speed by fifty percent, and descending the mountain increases its speed by twenty percent. If the distance going to the top of the mountain is 60 miles and the distance going down to the foot of the mountain is 72 miles, how many hours will Crystal have to pass the whole mountain?"""
    speed = 30
    uphill_speed = 0.5 * speed
    downhill_speed = 1.2 * speed
    uphill_distance = 60
    downhill_distance = 72
    uphill_time = uphill_distance / uphill_speed
    downhill_time = downhill_distance / downhill_speed
    total_time = uphill_time + downhill_time
    result = total_time
    return result

print(solution())