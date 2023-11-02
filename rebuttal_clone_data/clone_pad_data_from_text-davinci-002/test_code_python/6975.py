def solution():
    km_walked = 3
    hours_to_walk = 2
    speed = km_walked / hours_to_walk
    km_to_travel = 12
    time_to_travel = km_to_travel / speed
    time_to_travel_in_minutes = time_to_travel * 60
    result = time_to_travel_in_minutes
    return result

print(solution())