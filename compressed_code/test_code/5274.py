def solution():
    
    meso_pages_per_min = 15/5  
    tyler_pages_per_min = 15/3  
    combined_pages_per_min = meso_pages_per_min + tyler_pages_per_min
    total_time = 40 / combined_pages_per_min
    result = total_time
    return result

print(solution())