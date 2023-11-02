def solution():
    # Calculate the total number of runway trips per model
    total_trips_per_model = 2 * (2 + 3)

    # Calculate the total number of runway trips for all models
    total_trips = total_trips_per_model * 6

    # Calculate the total time for all runway trips
    total_time = total_trips * 2

    result = total_time
    return result

print(solution())