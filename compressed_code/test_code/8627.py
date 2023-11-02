def solution():
    
    total_pages = 354
    day1_pages = 63
    day2_pages = day1_pages * 2
    day3_pages = day2_pages + 10
    pages_read_so_far = day1_pages + day2_pages + day3_pages
    day4_pages = total_pages - pages_read_so_far
    result = day4_pages
    return result

print(solution())