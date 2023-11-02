def solution():
    
    pages_in_book = 381
    pages_read = 149
    pages_per_day = 20
    days = 7
    pages_to_read = pages_in_book - pages_read
    total_pages_read = pages_per_day * days
    pages_left = pages_to_read - total_pages_read
    result = pages_left
    return result

print(solution())