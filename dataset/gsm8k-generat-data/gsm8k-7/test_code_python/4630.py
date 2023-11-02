def solution():
    num_models = 6

    # Each model will do 2 trips for each set of bathing suits and 2 trips for each set of evening wear
    num_trips_per_model = (2 * 2) + (2 * 3)

    # Total number of trips for all models
    total_trips = num_models * num_trips_per_model

    # Time for each trip
    trip_time = 2

    # Total time for all trips
    total_time = total_trips * trip_time
    result = total_time
    return result

print(solution())