def solution():
    """James drives to Canada at 60 mph. It is a distance of 360 miles. He has a 1 hour stop along the way. How long does he take to get to Canada?"""
    distance = 360
    speed = 60
    time = distance / speed
    total_time = time + 1  # adding 1 hour for the stop
    result = total_time
    return result

print(solution())