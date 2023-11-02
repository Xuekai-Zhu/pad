def solution():
    pages_read = [10, 15, 27, 12, 19]
    total_pages_read = sum(pages_read)
    total_pages = total_pages_read * 3
    pages_left = total_pages - total_pages_read
    result = pages_left
    return result

print(solution())