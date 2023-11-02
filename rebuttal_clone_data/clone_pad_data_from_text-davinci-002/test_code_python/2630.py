def solution():
    hours_in_trip = 14
    stops_for_legs = hours_in_trip / 2
    stops_for_food = 2
    stops_for_gas = 3
    total_stops = stops_for_legs + stops_for_food + stops_for_gas
    minutes_per_stop = 20
    total_minutes = total_stops * minutes_per_stop
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())