def solution():
    
    planned_reading_time = 3 * 60  
    actual_reading_time = planned_reading_time * 0.75
    pages_per_minute = 1 / 15
    total_pages = int(pages_per_minute * actual_reading_time)
    result = total_pages
    return result

print(solution())