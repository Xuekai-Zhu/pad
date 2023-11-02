def solution():
    """Traveling from Manhattan to the Bronx, Andrew rides the subway for 10 hours, takes the train and rides for twice as much time as the subway ride, and then bikes the remaining distance for 8 hours. What's the total time he takes to reach the Bronx from Manhattan?"""
    subway_time = 10
    train_time = 2 * subway_time
    bike_time = 8
    total_time = subway_time + train_time + bike_time
    result = total_time
    return result

print(solution())