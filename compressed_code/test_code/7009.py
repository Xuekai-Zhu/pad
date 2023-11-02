def solution():
    
    cans_per_trip = 4
    time_to_drain = 30
    round_trip_time = 20
    total_cans = 28
    trips = total_cans // cans_per_trip + (total_cans % cans_per_trip > 0)
    total_time = trips * (time_to_drain + round_trip_time)
    result = total_time
    return result

print(solution())