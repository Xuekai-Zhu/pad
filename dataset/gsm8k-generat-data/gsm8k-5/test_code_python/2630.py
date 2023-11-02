def solution():
    total_trip_time = 14  # Carter has a 14-hour road trip
    num_leg_stretch_stops = 7  # If he stops every 2 hours, he will have 7 leg-stretching stops
    num_food_stops = 2  # He wants to make 2 additional stops for food
    num_gas_stops = 3  # He wants to make 3 additional stops for gas
    time_per_stop = 1 / 3  # Each pit stop is 20 minutes, or 1/3 of an hour

    # Calculate the total time spent on pit stops
    total_pit_stop_time = (num_leg_stretch_stops + num_food_stops + num_gas_stops) * time_per_stop

    # Calculate the total time for the road trip, including pit stops
    total_time = total_trip_time + total_pit_stop_time
    result = total_time
    return result

print(solution())