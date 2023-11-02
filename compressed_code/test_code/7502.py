def solution():
    
    total_pages = 381
    pages_read = 149
    pages_per_day = 20
    days_in_week = 7
    pages_left = total_pages - pages_read - (pages_per_day * days_in_week)
    result = pages_left
    return result

print(solution())