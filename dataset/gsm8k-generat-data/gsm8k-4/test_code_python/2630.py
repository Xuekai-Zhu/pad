def solution():
    """Carter has a 14-hour road trip. He wants to stop every 2 hours to stretch his legs. He also wants to make 2 additional stops for food and 3 additional stops for gas. If each pit stop takes 20 minutes, how many hours will his road trip become?"""
    # Define the total length of the road trip
    total_trip_length = 14

    # Define the number of stops for leg stretching, food, and gas
    leg_stretch_stops = total_trip_length // 2
    food_stops = 2
    gas_stops = 3

    # Calculate the total duration of all pit stops
    total_pit_stop_duration = 20 * (leg_stretch_stops + food_stops + gas_stops)

    # Calculate the total duration of the road trip, including pit stops
    total_duration = total_trip_length + (total_pit_stop_duration / 60)

    # Return the result
    result = total_duration
    return result

print(solution())