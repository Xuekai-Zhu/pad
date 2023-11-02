def solution():
    
    total_pages = 248
    pages_read_mon = 16 * 3
    pages_read_tue = 16 * 6.5
    pages_read = pages_read_mon + pages_read_tue
    pages_remaining = total_pages - pages_read
    hours_remaining = pages_remaining / 16
    result = hours_remaining
    return result

print(solution())