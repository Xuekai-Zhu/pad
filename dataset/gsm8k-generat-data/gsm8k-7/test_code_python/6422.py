def solution():
    run_time = 20
    jog_time = 10
    return_trip_multiplier = 3

    # Calculate the total time to get to the park
    total_time_to_park = run_time + jog_time

    # Calculate the total time for the return trip
    return_trip_time = total_time_to_park * return_trip_multiplier

    result = return_trip_time
    return result

print(solution())