def solution():
    """Sid traveled 110 miles in 2 hours. If Sid then traveled an additional 140 miles in 3 hours, what's the average speed he was traveling?"""
    distance1 = 110
    distance2 = 140
    time1 = 2
    time2 = 3
    total_distance = distance1 + distance2
    total_time = time1 + time2
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())