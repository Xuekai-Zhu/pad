def solution():
    
    total_pages = 93
    pages_read_saturday = 30
    pages_read_sunday = 20
    pages_remaining = total_pages - pages_read_saturday - pages_read_sunday
    result = pages_remaining
    return result

print(solution())