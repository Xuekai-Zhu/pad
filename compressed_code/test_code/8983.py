def solution():
    
    total_pages = 360
    pages_read_saturday = 40 + 10
    pages_read_sunday = 2 * pages_read_saturday
    pages_left = total_pages - pages_read_saturday - pages_read_sunday
    result = pages_left
    return result

print(solution())