def solution():
    number_of_cans = 28
    cans_per_trip = 4
    time_to_drain_cans = 30
    time_to_walk = 10
 
    number_of_trips = number_of_cans / cans_per_trip
    time_to_throw_away = (time_to_walk * 2) + (time_to_drain_cans * number_of_trips)
    result = time_to_throw_away
 
    return result

print(solution())