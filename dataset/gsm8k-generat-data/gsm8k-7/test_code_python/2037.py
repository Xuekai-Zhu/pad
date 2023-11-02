def solution():
    rhonda_speed = 200 / 24  # meters per second
    sally_speed = 200 / 26  # meters per second
    diane_speed = 200 / 21  # meters per second

    # Calculate the total time for the three of them to run the relay race
    total_time = 600 / (rhonda_speed + sally_speed + diane_speed)
    result = total_time
    return result

print(solution())