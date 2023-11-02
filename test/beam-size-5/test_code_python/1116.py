def solution():
    
    visits_per_month = 2
    speed = 70
    time_per_trip = 2
    distance_per_trip = speed * time_per_trip
    total_distance = visits_per_month * distance_per_trip
    result = total_distance
    return result

print(solution())