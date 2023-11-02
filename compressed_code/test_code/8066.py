def solution():
    
    total_pages = 120
    science_pages = total_pages * 0.25
    math_pages = 10
    remaining_pages = total_pages - science_pages - math_pages
    result = remaining_pages
    return result

print(solution())