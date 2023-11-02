def solution():
    pages_per_minute = 8 / 20  # Joy's reading speed in pages per minute
    pages_in_120 = 120  # Total number of pages to read
    minutes_to_read_120 = pages_in_120 / pages_per_minute  # Total minutes to read 120 pages
    hours_to_read_120 = minutes_to_read_120 / 60  # Convert minutes to hours
    result = hours_to_read_120
    return result

print(solution())