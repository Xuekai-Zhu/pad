def solution():
    """Emery's family decides to travel for a weekend trip. They drive the first 100 miles in 1 hour. They stop at a McDonald's and then continue the rest of the journey for 300 miles. What's the total number of hours they traveled?"""
    distance1 = 100
    time1 = 1
    distance2 = 300
    speed = (distance2 - distance1) / time2
    time2 = distance2 / speed
    total_time = time1 + time2
    result = total_time
    return result

print(solution())