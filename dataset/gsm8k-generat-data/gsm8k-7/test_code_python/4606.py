def solution():
    total_pages = 400
    percent_read = 0.2  # 20% read
    pages_read = total_pages * percent_read
    pages_left = total_pages - pages_read
    result = pages_left
    return result

print(solution())