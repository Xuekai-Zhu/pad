def solution():
    pages_read_Saturday = 30
    pages_read_Sunday = 20
    total_pages = 93
    pages_remaining = total_pages - (pages_read_Saturday + pages_read_Sunday)
    result = pages_remaining
    return result

print(solution())