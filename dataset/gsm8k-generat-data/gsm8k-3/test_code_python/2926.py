def solution():
    """Apple can run at a rate of 3 miles per hour. Mac can run at a rate of 4 miles per hour. In minutes, how much faster will Mac run a 24 mile race?"""
    # Calculate the time it takes for Apple to run the 24 mile race
    apple_time = 24 / 3  # time = distance / rate

    # Calculate the time it takes for Mac to run the 24 mile race
    mac_time = 24 / 4

    # Calculate the difference in time between Mac and Apple in minutes
    time_difference = (mac_time - apple_time) * 60  # convert to minutes

    # Display the time difference
    result = time_difference
    return result

print(solution())