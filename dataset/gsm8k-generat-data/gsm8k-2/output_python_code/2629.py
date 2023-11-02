def solution():
    """Carter has a 14-hour road trip. He wants to stop every 2 hours to stretch his legs. He also wants to make 2 additional stops for food and 3 additional stops for gas. If each pit stop takes 20 minutes, how many hours will his road trip become?"""
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