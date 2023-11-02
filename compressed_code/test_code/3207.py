def solution():
    
    total_pictures = 960
    process_time_per_picture = 2 
    total_process_time = total_pictures * process_time_per_picture 
    total_process_time_hours = total_process_time / 60 
    result = total_process_time_hours
    return result

print(solution())