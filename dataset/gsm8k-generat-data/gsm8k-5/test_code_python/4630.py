def solution():
    models = 6  # There are 6 models in the show
    sets_bathing_suits = 2  # Each model will wear 2 sets of bathing suits
    sets_evening_wear = 3  # Each model will wear 3 sets of evening wear clothing
    time_per_trip = 2  # It takes 2 minutes for a model to walk out to the end of the runway and back

    # Calculate the total number of runway trips
    total_trips = models * (sets_bathing_suits + sets_evening_wear)

    # Calculate the total time for all runway trips
    total_time = total_trips * time_per_trip
    result = total_time
    return result

print(solution())