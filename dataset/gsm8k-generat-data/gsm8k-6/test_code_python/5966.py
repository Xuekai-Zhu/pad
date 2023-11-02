def solution():
    total_pages = 500
    pages_read_night1 = 0.2 * total_pages
    pages_read_night2 = 0.2 * total_pages
    pages_read_night3 = 0.3 * total_pages
    total_pages_read = pages_read_night1 + pages_read_night2 + pages_read_night3
    pages_left = total_pages - total_pages_read
    result = pages_left
    return result

print(solution())