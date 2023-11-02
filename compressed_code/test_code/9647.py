def solution():
    
    total_pages = 30
    percent_to_read = 70
    percent_decimal = percent_to_read / 100
    pages_to_read_before_break = total_pages * percent_decimal
    pages_after_break = total_pages - pages_to_read_before_break
    result = pages_after_break
    return result

print(solution())