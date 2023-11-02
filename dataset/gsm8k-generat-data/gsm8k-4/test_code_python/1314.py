def solution():
    """A train travels 270 miles in 3 hours. At the same rate, how many additional hours would it take to travel an additional 180 miles?"""
    # Define the distance and time of the first trip
    distance_1 = 270
    time_1 = 3

    # Calculate the speed of the train
    speed = distance_1 / time_1

    # Define the distance of the second trip
    distance_2 = 180

    # Calculate the time it takes to travel the second distance
    time_2 = distance_2 / speed

    # return the result
    result = time_2 - time_1
    return result

print(solution())