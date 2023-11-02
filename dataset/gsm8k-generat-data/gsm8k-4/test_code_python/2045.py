def solution():
    """Traveling from Manhattan to the Bronx, Andrew rides the subway for 10 hours, takes the train and rides for twice as much time as the subway ride, and then bikes the remaining distance for 8 hours. What's the total time he takes to reach the Bronx from Manhattan?"""
    # Define the time spent on the subway and the time spent biking
    subway_time = 10
    biking_time = 8

    # Calculate the time spent on the train
    train_time = subway_time * 2

    # Calculate the total time
    total_time = subway_time + train_time + biking_time

    # Return the result
    result = total_time
    return result

print(solution())