def solution():
    minutes_to_ride = 15
    minutes_to_ski = 5
    minutes_in_two_hours = 120
    minutes_available = minutes_in_two_hours - minutes_to_ride
    skis_per_hour = minutes_available / minutes_to_ski
    result = skis_per_hour
    return result

print(solution())