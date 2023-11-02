def solution():
    total_pages = 100
    pages_read_yesterday = 35
    pages_to_read_today = pages_read_yesterday - 5
    pages_to_read_tomorrow = total_pages - (pages_read_yesterday + pages_to_read_today)
    result = pages_to_read_tomorrow
    return result

print(solution())