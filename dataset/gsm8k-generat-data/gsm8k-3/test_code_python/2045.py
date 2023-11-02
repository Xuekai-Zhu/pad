def solution():
    """Traveling from Manhattan to the Bronx, Andrew rides the subway for 10 hours, takes the train and rides for twice as much time as the subway ride, and then bikes the remaining distance for 8 hours. What's the total time he takes to reach the Bronx from Manhattan?"""
    # Define the time for subway ride and bike ride
    subway_time = 10
    bike_time = 8

    # Calculate the time for train ride
    train_time = subway_time * 2

    # Calculate the total time
    total_time = subway_time + train_time + bike_time

    # Display the total time
    result = total_time
    return result

print(solution())