def solution():
    
    total_pages = 4 + 20 + 7 + 8
    pages_left = total_pages - 15
    days_left = 4
    average_pages_per_day = pages_left / days_left
    result = average_pages_per_day
    return result

print(solution())