def solution():
    ride_time = 15  # The time it takes to ride the lift from bottom to top in minutes
    ski_time = 5  # The time it takes to ski down the mountain in minutes
    total_time = 120  # The total time available in minutes

    # Calculate the time taken for each round trip (up and down the mountain)
    round_trip_time = ride_time + ski_time

    # Calculate the maximum number of round trips possible in the given time
    max_round_trips = total_time // round_trip_time

    result = max_round_trips
    return result

print(solution())