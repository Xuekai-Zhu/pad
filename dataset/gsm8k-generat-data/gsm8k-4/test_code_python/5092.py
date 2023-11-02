def solution():
    """Kevin is taking a 600-mile trip, traveling at a rate of 50 miles per hour. How much faster must he travel to decrease his travel time by 4 hours?"""
    # Define the initial speed and distance
    initial_speed = 50
    distance = 600

    # Calculate the initial travel time
    initial_time = distance / initial_speed

    # Calculate the desired travel time with a 4-hour decrease
    desired_time = initial_time - 4

    # Calculate the required speed to achieve the desired travel time
    required_speed = distance / desired_time

    # Calculate the speed difference
    speed_difference = required_speed - initial_speed

    result = speed_difference
    return result

print(solution())