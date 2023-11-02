def solution():
    total_pages = 400
    percentage_read = 20
    pages_read = (percentage_read / 100) * total_pages
    pages_remaining = total_pages - pages_read
    result = pages_remaining
    return result

print(solution())