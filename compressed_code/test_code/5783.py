def solution():
    
    total_pages = 120
    pages_read_yesterday = 12
    pages_read_today = 2 * pages_read_yesterday
    pages_left = total_pages - pages_read_yesterday - pages_read_today
    pages_to_read_tomorrow = pages_left / 2
    result = pages_to_read_tomorrow
    return result

print(solution())