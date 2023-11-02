def solution():
    ride_time = 15  # minutes
    ski_time = 5   # minutes
    total_time = 120   # minutes (2 hours)
    
    # Calculate the total time for one round trip (up and down the mountain)
    round_trip_time = ride_time + ski_time
    
    # Calculate the maximum number of round trips a person can make in two hours
    max_round_trips = total_time // round_trip_time
    
    result = max_round_trips
    return result

print(solution())