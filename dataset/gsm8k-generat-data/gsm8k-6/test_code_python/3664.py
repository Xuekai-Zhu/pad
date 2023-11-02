def solution():
    # Calculate the total time taken by Bob to complete the race
    total_time = 70 + 85 + 85  # in seconds

    # Convert the total time to minutes
    total_time = total_time / 60

    # Calculate the total distance covered by Bob
    total_distance = 3 * 400  # Bob runs 3 laps of 400 meters each

    # Calculate the average speed of Bob in m/s
    average_speed = total_distance / (total_time * 60)

    result = average_speed
    return result

print(solution())