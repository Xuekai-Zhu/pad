def solution():
    """Erik's dog can run 24 miles per hour. It is chasing a rabbit that can run 15 miles per hour. The rabbit has a head start of .6 miles. How many minutes does it take for the dog to catch up to the rabbit?"""
    # Define the speeds of the dog and rabbit
    DOG_SPEED = 24
    RABBIT_SPEED = 15

    # Define the head start distance of the rabbit
    HEAD_START = 0.6

    # Calculate the relative speed between the dog and rabbit
    relative_speed = DOG_SPEED - RABBIT_SPEED

    # Calculate the time it takes for the dog to catch up to the rabbit
    catch_up_time = HEAD_START / relative_speed

    # Convert the catch-up time to minutes
    catch_up_time_min = catch_up_time * 60

    # Display the time it takes for the dog to catch up to the rabbit
    result = catch_up_time_min
    return result

print(solution())