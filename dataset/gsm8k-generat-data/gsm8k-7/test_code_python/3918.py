def solution():
    pages_read = 10 + 15 + 27 + 12 + 19  # Total pages read
    total_pages = pages_read * 3  # Total number of pages in the book
    pages_left = total_pages - pages_read  # Number of pages Jesse still needs to read
    result = pages_left
    return result

print(solution())