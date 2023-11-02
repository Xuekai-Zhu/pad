def solution():
    distance1 = 3  # Ben walked 3 km in 2 hours
    time1 = 2 * 60  # Convert 2 hours to minutes

    speed = distance1 / time1  # Calculate his speed in km/minute

    distance2 = 12  # Ben needs to travel 12 km
    time2 = distance2 / speed  # Calculate the time it will take him to travel 12 km at the same speed

    result = time2 * 60  # Convert time to minutes
    return result

print(solution())