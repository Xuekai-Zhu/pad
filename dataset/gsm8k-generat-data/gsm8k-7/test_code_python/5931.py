def solution():
    total_distance = 15  # assume distance from house to water park is 15 miles
    time_driving_slow = 0.25 * 0.5  # 30 mins * half the journey = 15 mins = 0.25 hours
    time_driving_fast = 0.25 * 0.5  # 30 mins * half the journey = 15 mins = 0.25 hours
    distance_driven_slow = time_driving_slow * 28
    distance_driven_fast = time_driving_fast * 60
    total_biking_distance = total_distance - (distance_driven_slow + distance_driven_fast)
    biking_speed = 11
    biking_time = total_biking_distance / biking_speed
    result = biking_time
    return result

print(solution())