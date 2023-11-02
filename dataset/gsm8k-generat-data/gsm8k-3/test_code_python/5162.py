def solution():
    """A train travels 360 miles in 3 hours. At the same rate, how many additional hours would it take to travel an additional 240 miles?"""
    # Define the distance and time for the first part of the trip
    distance1 = 360
    time1 = 3

    # Calculate the rate of the train
    rate = distance1 / time1

    # Calculate the time it would take for the train to travel the additional distance
    distance2 = 240
    time2 = distance2 / rate

    # Display the additional time needed
    result = time2 - time1
    return result

print(solution())