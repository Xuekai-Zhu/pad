def solution():
    pages_written = [25, 50, 100, 10]
    total_pages = 500
    pages_remaining = total_pages - sum(pages_written)
    result = pages_remaining
    return result

print(solution())