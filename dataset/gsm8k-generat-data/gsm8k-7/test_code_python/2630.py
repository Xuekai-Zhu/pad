def solution():
    road_trip_hours = 14
    leg_stretch_stops = 7  # one stop every 2 hours
    food_stops = 2
    gas_stops = 3
    pit_stop_time = 20 / 60  # convert minutes to hours

    # Calculate the total time spent on pit stops
    total_pit_stop_time = (leg_stretch_stops + food_stops + gas_stops) * pit_stop_time

    # Calculate the total time of the road trip including pit stops
    total_time = road_trip_hours + total_pit_stop_time
    result = total_time
    return result

print(solution())