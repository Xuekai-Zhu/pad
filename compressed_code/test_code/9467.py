def solution():
    
    distance_to_idaho = 640
    distance_to_nevada = 550
    speed_to_idaho = 80
    speed_to_nevada = 50
    
    time_to_idaho = distance_to_idaho / speed_to_idaho
    time_to_nevada = distance_to_nevada / speed_to_nevada
    
    total_time = time_to_idaho + time_to_nevada
    
    result = total_time
    
    return result

print(solution())