def solution():
    """Apple can run at a rate of 3 miles per hour. Mac can run at a rate of 4 miles per hour. In minutes, how much faster will Mac run a 24 mile race?"""
    # Define the distances and speeds
    distance = 24
    apple_speed = 3
    mac_speed = 4

    # Calculate the time taken by each to complete the race
    apple_time = distance / apple_speed
    mac_time = distance / mac_speed

    # Calculate the time difference between Mac and Apple
    time_difference = mac_time - apple_time

    # Convert the time difference to minutes
    time_difference_minutes = time_difference * 60

    # Return the result
    result = time_difference_minutes
    return result

print(solution())