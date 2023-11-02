def solution():
    
    fast_lane_speed = 60
    slow_lane_speed = fast_lane_speed / 2
    total_distance = 480
    slow_lane_distance = total_distance / slow_lane_speed
    time_taken = slow_lane_distance / fast_lane_speed
    result = time_taken
    return result

print(solution())