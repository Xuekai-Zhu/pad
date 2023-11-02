def solution():
    
    total_pages = 600
    days_available = 30 - 4 - 1  
    remaining_pages = total_pages - 100  
    pages_per_day = remaining_pages / days_available
    result = pages_per_day
    return result

print(solution())