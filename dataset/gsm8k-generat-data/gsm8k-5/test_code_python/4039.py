def solution():
    total_distance = 300  # Jenna and her friend will be driving a total of 300 miles
    jenna_distance = 200  # Jenna will drive the first 200 miles
    friend_distance = 100  # Her friend will drive the last 100 miles
    jenna_speed = 50  # Jenna will drive at a speed of 50 miles per hour
    friend_speed = 20  # Her friend will drive at a speed of 20 miles per hour
    num_breaks = 2  # They will take 2 30-minute breaks

    # Calculate the time it takes Jenna to drive her portion of the trip
    jenna_time = jenna_distance / jenna_speed

    # Calculate the time it takes her friend to drive the remaining portion of the trip
    friend_time = friend_distance / friend_speed

    # Calculate the total driving time for the trip
    total_time = jenna_time + friend_time

    # Add in the time for the breaks
    total_time += num_breaks * 0.5

    result = total_time
    return result

print(solution())