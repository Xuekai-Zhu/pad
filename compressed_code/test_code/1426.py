def solution():
    
    start_time = 6 * 60  
    first_station_time = 40  
    end_time = 9 * 60  
    total_travel_time = end_time - (start_time + first_station_time)
    result = total_travel_time
    return result

print(solution())