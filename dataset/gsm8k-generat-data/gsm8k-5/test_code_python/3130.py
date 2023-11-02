def solution():
    speed = 60  # Jace drives 60 miles per hour
    time1 = 4  # Jace drives for 4 hours straight
    time2 = 9  # Jace drives for 9 hours straight after taking a 30-minute break
    break_time = 0.5  # Jace takes a 30-minute break

    # Calculate the distance Jace travels in the first leg of the trip
    distance1 = speed * time1

    # Calculate the distance Jace travels in the second leg of the trip
    distance2 = speed * time2

    # Calculate the total distance Jace travels
    total_distance = distance1 + distance2

    # Subtract the distance Jace covers during his break
    total_distance -= speed * break_time

    result = total_distance
    return result

print(solution())