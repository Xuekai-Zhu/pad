def solution():
    total_pages = 30
    percent_to_read_before_break = 0.7
    
    # Calculate the number of pages to read before taking a break
    pages_before_break = total_pages * percent_to_read_before_break
    
    # Calculate the remaining pages to be read after the break
    pages_after_break = total_pages - pages_before_break
    
    result = pages_after_break
    return result

print(solution())