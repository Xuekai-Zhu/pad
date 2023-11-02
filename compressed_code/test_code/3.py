def solution():
    
    total_pages = 120
    yesterday_pages = 12
    today_pages = 2 * yesterday_pages
    remaining_pages = total_pages - yesterday_pages - today_pages
    half_remaining_pages = remaining_pages / 2
    pages_to_read_tomorrow = half_remaining_pages
    result = pages_to_read_tomorrow
    return result

print(solution())