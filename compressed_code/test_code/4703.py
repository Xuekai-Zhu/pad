def solution():
    
    total_pages = 500
    day1_pages = 25
    day2_pages = 2 * day1_pages
    day3_pages = 2 * day2_pages
    day4_pages = 10
    total_written_pages = day1_pages + day2_pages + day3_pages + day4_pages
    remaining_pages = total_pages - total_written_pages
    result = remaining_pages
    return result

print(solution())