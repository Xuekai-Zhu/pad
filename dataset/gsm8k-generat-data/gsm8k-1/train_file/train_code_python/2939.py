def solution():
    """Chrystal’s vehicle speed is 30 miles per hour. Ascending the mountain decreases its speed by fifty percent, and descending the mountain increases its speed by twenty percent. If the distance going to the top of the mountain is 60 miles and the distance going down to the foot of the mountain is 72 miles, how many hours will Crystal have to pass the whole mountain?"""
    initial_speed = 30
    top_distance = 60
    bottom_distance = 72
    uphill_speed = initial_speed * 0.5
    downhill_speed = initial_speed * 1.2
    time_uphill = top_distance / uphill_speed
    time_downhill = bottom_distance / downhill_speed
    total_time = time_uphill + time_downhill
    result = total_time
    return result

print(solution())