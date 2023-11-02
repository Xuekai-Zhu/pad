def solution():
    subway_ride = 10  # Andrew rides the subway for 10 hours
    train_ride = subway_ride * 2  # Andrew takes the train for twice as much time as the subway ride
    biking_time = 8  # Andrew bikes the remaining distance for 8 hours

    # Calculate the total time Andrew takes to reach the Bronx
    total_time = subway_ride + train_ride + biking_time
    result = total_time
    return result

print(solution())