def solution():
    
    cans_on_desk = 28
    cans_per_trip = 4
    drain_time = 30
    walk_time = 10
    total_trips = cans_on_desk // cans_per_trip + (1 if cans_on_desk % cans_per_trip > 0 else 0)
    total_time = total_trips * (drain_time + 2 * walk_time)
    result = total_time
    return result

print(solution())