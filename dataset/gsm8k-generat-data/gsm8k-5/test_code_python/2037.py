def solution():
    # Calculate the time it takes for Rhonda to run 200 meters
    rhonda_time = 24

    # Calculate the time it takes for Sally to run 200 meters
    sally_time = rhonda_time + 2

    # Calculate the time it takes for Diane to run 200 meters
    diane_time = rhonda_time - 3

    # Calculate the total time for the relay race
    total_time = rhonda_time + sally_time + diane_time

    # Multiply the total time by 3 since there are 3 runners in the relay
    result = total_time * 3
    return result

print(solution())