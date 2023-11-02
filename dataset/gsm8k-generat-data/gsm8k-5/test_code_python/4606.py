def solution():
    total_pages = 400  # The book has 400 pages
    pages_read = total_pages * 0.2  # Nate has already read 20% of the book
    pages_remaining = total_pages - pages_read  # Nate needs to read the remaining pages
    result = pages_remaining
    return result

print(solution())