def solution():
    
    drive_time = 195  
    airport_time = 30  
    flight_time = drive_time / 3
    destination_time = 10
    airplane_total_time = airport_time + flight_time + destination_time
    time_saved = drive_time - airplane_total_time
    result = time_saved
    
    return result

print(solution())