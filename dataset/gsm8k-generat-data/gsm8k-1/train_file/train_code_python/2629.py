def solution():
    """Carter has a 14-hour road trip. He wants to stop every 2 hours to stretch his legs. He also wants to make 2 additional stops for food and 3 additional stops for gas. If each pit stop takes 20 minutes, how many hours will his road trip become?"""
    total_hours = 14
    leg_stretch_stops = total_hours // 2
    food_stops = 2
    gas_stops = 3
    total_stops = leg_stretch_stops + food_stops + gas_stops
    time_per_stop = 20 / 60  # converting 20 minutes to hours
    total_time_added = total_stops * time_per_stop
    total_travel_time = total_hours + total_time_added
    result = total_travel_time
    return result

print(solution())