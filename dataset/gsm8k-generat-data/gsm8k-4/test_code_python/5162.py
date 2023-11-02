def solution():
    """A train travels 360 miles in 3 hours. At the same rate, how many additional hours would it take to travel an additional 240 miles?"""
    # Define the initial distance and time
    initial_distance = 360
    initial_time = 3

    # Define the additional distance
    additional_distance = 240

    # Calculate the speed of the train
    speed = initial_distance / initial_time

    # Calculate the additional time needed to travel the additional distance
    additional_time = additional_distance / speed

    # Return the result
    result = additional_time - initial_time
    return result

print(solution())