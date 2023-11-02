def solution():
    """Emery's family decides to travel for a weekend trip. They drive the first 100 miles in 1 hour. They stop at a McDonald's and then continue the rest of the journey for 300 miles. What's the total number of hours they traveled?"""
    distance_1 = 100
    time_1 = 1
    distance_2 = 300
    speed = distance_2 / (time_2 - time_1)
    time_2 = time_1 + (distance_2 / speed)
    total_time = time_2
    result = total_time
    return result

print(solution())