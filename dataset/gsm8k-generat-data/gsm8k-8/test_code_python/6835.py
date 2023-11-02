def solution():
    # Define the total time available in minutes
    total_time = 120

    # Calculate the time it takes for each round trip in minutes
    round_trip_time = 15 + 5

    # Calculate the number of round trips possible in the available time
    num_round_trips = total_time // round_trip_time

    result = num_round_trips
    return result

print(solution())