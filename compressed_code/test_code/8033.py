def solution():
    
    planned_time = 3 
    actual_time = planned_time * 0.75 
    time_per_page = 15 
    pages_read = actual_time * 60 / time_per_page
    result = pages_read
    return result

print(solution())