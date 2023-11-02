def solution():
    
    total_pages = 30
    percent_before_break = 0.7
    pages_before_break = total_pages * percent_before_break
    pages_after_break = total_pages - pages_before_break
    result = pages_after_break
    return result

print(solution())