def solution():
    
    pages_per_minute = 8/20
    minutes_to_read_120_pages = 120 / pages_per_minute
    hours_to_read_120_pages = minutes_to_read_120_pages / 60
    result = hours_to_read_120_pages
    return result

print(solution())