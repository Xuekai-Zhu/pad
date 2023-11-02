def solution():
    speed1 = 10  # miles per hour
    time1 = 0.5  # hours
    distance1 = speed1 * time1

    speed2 = 20  # miles per hour
    time2 = 0.5  # hours
    distance2 = speed2 * time2

    speed3 = 8  # miles per hour
    time3 = 0.25  # hours (15 minutes is 0.25 hours)
    distance3 = speed3 * time3

    # Calculate the total distance that Kevin ran
    total_distance = distance1 + distance2 + distance3
    result = total_distance
    return result

print(solution())