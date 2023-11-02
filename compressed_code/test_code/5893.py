def solution():
    
    floors_per_flight = 3
    up_flights_per_day = 5
    down_flights_per_day = 3
    total_flights_per_day = (up_flights_per_day + down_flights_per_day) * floors_per_flight
    result = total_flights_per_day
    return result

print(solution())