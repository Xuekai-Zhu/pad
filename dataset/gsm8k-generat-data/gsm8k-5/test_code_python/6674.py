def solution():
    total_travel_time = 13  # William left at 7:00 AM and arrived at 8:00 PM, so he spent 13 hours traveling
    time_spent_stops = 60 + 25 + 10 + 25  # William had 3 stops, with durations of 25, 10, and 25 minutes
    road_time = total_travel_time - (time_spent_stops / 60)  # Convert time spent at stops from minutes to hours

    result = road_time
    return result

print(solution())