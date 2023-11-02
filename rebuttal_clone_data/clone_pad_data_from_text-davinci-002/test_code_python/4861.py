def solution():
    pages_read_per_minute = 4
    minutes_to_read_4_pages = 2
    total_pages = 18
    minutes_to_read_18_pages = total_pages / pages_read_per_minute * minutes_to_read_4_pages
    result = minutes_to_read_18_pages
    return result

print(solution())