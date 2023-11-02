def solution():
    
    trips_to_park = 6
    time_at_park = 2
    walking_time = 0.5
    total_time = (time_at_park + walking_time) * trips_to_park
    percent_at_park = (time_at_park * trips_to_park / total_time) * 100
    result = percent_at_park
    
    return result

print(solution())