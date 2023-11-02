def solution():
    apple_speed = 3  # Apple runs at a rate of 3 miles per hour
    mac_speed = 4  # Mac runs at a rate of 4 miles per hour
    distance = 24  # The race is 24 miles long

    # Calculate the time it will take for Apple to run the race
    apple_time = distance / apple_speed

    # Calculate the time it will take for Mac to run the race
    mac_time = distance / mac_speed

    # Calculate the difference in time between Mac and Apple
    time_difference = mac_time - apple_time

    # Convert the time difference to minutes
    minutes_difference = time_difference * 60
    result = minutes_difference
    return result

print(solution())