def solution():
    
    road_trip_hours = 14
    num_leg_stops = road_trip_hours // 2
    num_food_stops = 2
    num_gas_stops = 3
    total_stops = num_leg_stops + num_food_stops + num_gas_stops
    stop_time = total_stops * 20 / 60
    total_time = road_trip_hours + stop_time
    result = total_time
    return result

print(solution())