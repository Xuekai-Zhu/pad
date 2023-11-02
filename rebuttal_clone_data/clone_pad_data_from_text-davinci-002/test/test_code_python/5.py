def solution():
    
    commute_distance = 40
    commute_time = commute_distance / 25
    commute_times_per_week = 5
    weekend_ride_distance = 200
    weekend_ride_time = weekend_ride_distance / 25
    total_time = (commute_times_per_week * commute_time) + weekend_ride_time
    result = total_time
    return result

print(solution())