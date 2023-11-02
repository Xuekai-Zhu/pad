def solution():
    
    num_flights = 20
    time_per_flight = 11
    total_time_running = num_flights * time_per_flight
    time_left = 72 - (total_time_running - 165)
    result = time_left
    return result

print(solution())