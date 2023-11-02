def solution():
    distance = 80
    time = 2  # in hours

    # Calculate the average speed of Luis
    speed = distance / time  # in miles per hour

    # Convert 15 minutes to hours
    time_in_hours = 15 / 60  # 0.25 hours

    # Calculate the distance Luis will go in 15 minutes
    distance_in_15_minutes = speed * time_in_hours  # in miles
    result = distance_in_15_minutes
    return result

print(solution())