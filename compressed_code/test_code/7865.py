def solution():
    
    total_hours = 14
    leg_stretch_stops = total_hours // 2
    food_stops = 2
    gas_stops = 3
    total_stops = leg_stretch_stops + food_stops + gas_stops
    time_per_stop = 20 / 60  
    total_time_added = total_stops * time_per_stop
    total_travel_time = total_hours + total_time_added
    result = total_travel_time
    return result

print(solution())