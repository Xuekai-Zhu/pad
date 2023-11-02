def solution():
    distance = 1200  # Melinda is taking a 1200-mile trip
    speed1 = 50  # Melinda's original speed is 50 miles per hour
    speed2 = 60  # Melinda's new speed is 60 miles per hour

    # Calculate the time it takes to travel at the original speed
    time1 = distance / speed1

    # Calculate the time it takes to travel at the new speed
    time2 = distance / speed2

    # Calculate the time difference
    time_difference = time1 - time2
    result = time_difference
    return result

print(solution())