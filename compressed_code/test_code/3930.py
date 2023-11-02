def solution():
    
    total_pages = 100
    days_left = 3 - 2  
    pages_per_day = (total_pages - 35 - (35 - 5)) / days_left
    result = pages_per_day
    return result

print(solution())