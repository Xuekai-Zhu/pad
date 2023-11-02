def solution():
    running_speed = 15
    swinging_speed = 10
    time_running = 5
    time_swinging = 10
    distance_running = running_speed * time_running
    distance_swinging = swinging_speed * time_swinging
    total_distance = distance_running + distance_swinging
    result = total_distance
    return result

print(solution())