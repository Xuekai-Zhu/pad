def solution():
    """
    Cora started reading a 158-page book on Monday, and she decided she wanted to finish it by the end of Friday. She read 23
    pages on Monday, 38 pages on Tuesday, and 61 pages on Wednesday. She knows she will have time to read twice as much on
    Friday as she does on Thursday. How many pages does she have to read on Thursday to finish the book in time?
    """
    total_pages = 158
    pages_read_so_far = 23 + 38 + 61
    pages_left_to_read = total_pages - pages_read_so_far
    
    pages_to_read_on_friday = pages_to_read_on_thursday * 2
    days_left_to_read = 2  # Thursday and Friday
    
    pages_to_read_on_thursday = pages_left_to_read / days_left_to_read
    
    result = pages_to_read_on_thursday
    return result

print(solution())