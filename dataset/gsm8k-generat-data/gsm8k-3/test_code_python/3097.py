def solution():
    """Theon's ship can move 15 nautical miles per hour while Yara's ship can move 30 nautical miles per hour. If their destination is 90 nautical miles away, how many hours ahead will Yara be ahead of Theon?"""
    # Define the speeds of Theon's and Yara's ships
    theon_speed = 15
    yara_speed = 30

    # Define the distance to their destination
    distance = 90

    # Calculate the time it will take for Theon to reach the destination
    theon_time = distance / theon_speed

    # Calculate the time it will take for Yara to reach the destination
    yara_time = distance / yara_speed

    # Calculate the time difference between Yara and Theon's arrival
    time_difference = yara_time - theon_time

    # Display the time difference
    result = time_difference
    return result

print(solution())