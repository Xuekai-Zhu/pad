def solution():
    pages_read_Saturday_morning = 40
    pages_read_Saturday_night = 10
    pages_read_Sunday = (pages_read_Saturday_morning + pages_read_Saturday_night) * 2
    total_pages_read = pages_read_Saturday_morning + pages_read_Saturday_night + pages_read_Sunday
    book_length = 360
    pages_left_to_read = book_length - total_pages_read
    
    result = pages_left_to_read
    
    return result

print(solution())