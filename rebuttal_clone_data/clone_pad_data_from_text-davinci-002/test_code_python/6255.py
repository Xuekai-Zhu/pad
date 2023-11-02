def solution():
    total_pages = 372
    pages_read = 125
    pages_skipped = 16
    pages_left = total_pages - pages_read - pages_skipped
    result = pages_left
    return result

print(solution())