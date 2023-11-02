def solution():
    
    start_time = 8  
    end_time = 12  
    total_work_time = (end_time - start_time) * 60  
    total_laundry = 80
    laundry_per_minute = total_laundry / total_work_time
    laundry_per_hour = laundry_per_minute * 60
    result = laundry_per_hour
    return result

print(solution())