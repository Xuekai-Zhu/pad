def solution():
    # Define the variables
    road_trip_time = 14
    num_leg_stops = road_trip_time // 2
    num_food_stops = 2
    num_gas_stops = 3
    pit_stop_time = 20/60

    # Calculate the total time spent on pit stops
    total_pit_stop_time = (num_leg_stops + num_food_stops + num_gas_stops) * pit_stop_time

    # Calculate the total time for the road trip, including pit stops
    total_time = road_trip_time + total_pit_stop_time

    result = total_time
    return result

print(solution())