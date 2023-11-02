def solution():
    """Erik's dog can run 24 miles per hour. It is chasing a rabbit that can run 15 miles per hour. The rabbit has a head start of .6 miles. How many minutes does it take for the dog to catch up to the rabbit?"""
    # Define the speeds of the dog and the rabbit, and the distance the rabbit has already traveled
    dog_speed = 24
    rabbit_speed = 15
    rabbit_distance = 0.6

    # Calculate how long it will take for the dog to catch up with the rabbit
    dog_time_to_catch_up = rabbit_distance / (dog_speed - rabbit_speed)

    # Convert the time to minutes
    minutes_to_catch_up = dog_time_to_catch_up * 60

    result = round(minutes_to_catch_up)
    return result

print(solution())