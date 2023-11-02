def solution():
    
    trip_distance = 2790
    driving_speed = 62
    driving_time = trip_distance / driving_speed
    num_breaks = driving_time // 5
    break_time = num_breaks * 0.5
    hotel_search_time = 0.5
    total_time = driving_time + break_time + hotel_search_time
    result = total_time
    return result

print(solution())