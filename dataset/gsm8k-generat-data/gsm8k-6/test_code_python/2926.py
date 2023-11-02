def solution():
    # Calculate the time it takes Apple and Mac to run a 24 mile race
    time_apple = 24 / 3  # Apple runs at a rate of 3 miles per hour
    time_mac = 24 / 4  # Mac runs at a rate of 4 miles per hour

    # Calculate the time difference between Apple and Mac
    time_difference = time_apple - time_mac

    # Convert the time difference to minutes
    time_difference_minutes = time_difference * 60

    result = time_difference_minutes
    return result

print(solution())