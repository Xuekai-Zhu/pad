def solution():
    
    total_pages = 360
    saturday_pages = 40 + 10
    sunday_pages = 2 * saturday_pages
    pages_read = saturday_pages + sunday_pages
    pages_left = total_pages - pages_read
    result = pages_left
    return result

print(solution())