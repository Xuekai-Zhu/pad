def solution():
    
    trips_per_day = 4
    max_passengers_per_trip = 12
    passengers_per_day = trips_per_day * max_passengers_per_trip
    passengers_in_two_days = passengers_per_day * 2
    result = passengers_in_two_days
    return result

print(solution())