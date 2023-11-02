def solution():
    original_distance = 40
    original_time = 5
    new_speed_increase = 0.4
    new_time = 10

    # Calculate the new distance Georgie can run using the speed increase
    new_distance = original_distance * (1 + new_speed_increase)

    # Calculate the new speed (distance over time)
    new_speed = new_distance / original_time

    # Calculate the new distance he can run in 10 seconds
    new_distance_in_10_seconds = new_speed * new_time
    result = new_distance_in_10_seconds
    return result

print(solution())