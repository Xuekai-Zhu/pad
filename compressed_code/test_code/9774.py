def solution():
    
    total_pages = 100
    days_left = 3 - 2    
    pages_read_yesterday = 35
    pages_read_today = pages_read_yesterday - 5
    pages_left = total_pages - pages_read_yesterday - pages_read_today
    pages_to_read_tomorrow = pages_left / days_left
    result = pages_to_read_tomorrow
    return result

print(solution())