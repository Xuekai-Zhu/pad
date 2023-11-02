def solution():
    driving_time = 30
    total_driving_distance = 28 + 60
    driving_speed = total_driving_distance / driving_time
    bike_speed = 11
    total_bike_distance = total_driving_distance
    bike_time = total_bike_distance / bike_speed
    result = bike_time
    
    return result

print(solution())