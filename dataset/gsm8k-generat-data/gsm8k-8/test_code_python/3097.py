def solution():
    # Define the speed of Theon's ship
    theon_speed = 15

    # Define the speed of Yara's ship
    yara_speed = 30

    # Define the total distance to travel
    distance = 90

    # Calculate the time it will take for Theon to reach the destination
    theon_time = distance / theon_speed

    # Calculate the time it will take for Yara to reach the destination
    yara_time = distance / yara_speed

    # Calculate the time difference between Yara and Theon
    time_difference = yara_time - theon_time

    result = time_difference
    return result

print(solution())