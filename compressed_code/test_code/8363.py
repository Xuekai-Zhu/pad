def solution():
    
    initial_passengers = 50
    passengers_added_first_stop = 16
    passengers_left_other_stops = 22
    passengers_added_other_stops = 5
    total_passengers = initial_passengers + passengers_added_first_stop - passengers_left_other_stops + passengers_added_other_stops
    result = total_passengers
    return result

print(solution())