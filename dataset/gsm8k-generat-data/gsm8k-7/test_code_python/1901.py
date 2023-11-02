def solution():
    total_distance = 200
    distance_traveled = total_distance * (1/4)
    time_spent_driving = 1
    remaining_distance = total_distance - distance_traveled
    speed = distance_traveled / time_spent_driving
    time_remaining = remaining_distance / speed
    total_time = time_spent_driving + 1 + time_remaining
    result = total_time
    return result

print(solution())