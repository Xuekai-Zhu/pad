def solution():
    
    distance_to_travel = 200
    speed_big_sail = 50
    speed_small_sail = 20
    time_big_sail = distance_to_travel / speed_big_sail
    time_small_sail = distance_to_travel / speed_small_sail
    time_difference = time_small_sail - time_big_sail
    result = time_difference
    return result

print(solution())