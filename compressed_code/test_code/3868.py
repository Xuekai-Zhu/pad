def solution():
    
    trips_per_month = 2
    total_trips_per_year = 12 * trips_per_month
    round_trip_time = 3
    total_drive_time_per_year = total_trips_per_year * round_trip_time
    result = total_drive_time_per_year
    return result

print(solution())