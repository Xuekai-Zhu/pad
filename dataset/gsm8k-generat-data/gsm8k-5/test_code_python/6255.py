def solution():
    total_pages = 372  # The book has 372 pages
    pages_read = 125  # Rich has already read 125 pages
    pages_skipped = 16  # The book has 16 pages of maps that Rich skipped

    # Calculate the number of pages left to read
    pages_left = total_pages - pages_read - pages_skipped
    result = pages_left
    return result

print(solution())