def solution():
    
    distance_per_trip = 1
    trips_per_day = 2
    days_per_week = 5
    total_distance_per_week = distance_per_trip * trips_per_day * days_per_week
    total_distance_after_four_weeks = total_distance_per_week * 4
    result = total_distance_after_four_weeks
    return result

print(solution())