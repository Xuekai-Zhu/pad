def solution():
    """Bob runs 6 miles per hour. His friend Jim runs at 9 miles per hour. If Bob has a 1 mile head-start, how many minutes will it take before Jim catches him?"""
    # Define the speeds of Bob and Jim in miles per minute
    BOB_SPEED = 0.1  # 6 mph = 0.1 miles per minute
    JIM_SPEED = 0.15  # 9 mph = 0.15 miles per minute

    # Define the distance of Bob's head-start in miles
    HEAD_START = 1

    # Calculate the time it takes for Jim to catch up to Bob in minutes
    time = HEAD_START / (JIM_SPEED - BOB_SPEED)

    # Convert the time to minutes
    time_minutes = time * 60

    # Display the time in minutes
    result = time_minutes
    return result

print(solution())