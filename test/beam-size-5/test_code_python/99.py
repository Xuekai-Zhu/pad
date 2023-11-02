def solution():
    
    distance_to_inland_edge = 42
    time_per_3_mph = 10
    distance_to_cover = distance_to_inland_edge / 3
    total_time = distance_to_cover * time_per_3_mph
    result = total_time
    return result

print(solution())