def solution():
    # Calculate the time Rhonda takes to run 200 meters
    rhonda_time = 24

    # Calculate Sally's time to run 200 meters, using the fact that she runs 2 seconds slower than Rhonda
    sally_time = rhonda_time + 2

    # Calculate Diane's time to run 200 meters, using the fact that she runs 3 seconds faster than Rhonda
    diane_time = rhonda_time - 3

    # Calculate the total time for the three of them to run the 600-meter relay race
    total_time = rhonda_time + sally_time + diane_time

    result = total_time
    return result

print(solution())