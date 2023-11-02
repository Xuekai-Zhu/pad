def solution():
    # Define the total number of pages and the number of pages already read
    total_pages = 372
    pages_read = 125

    # Subtract the pages read and the pages skipped from the total number of pages to find the remaining pages
    remaining_pages = total_pages - pages_read - 16
    result = remaining_pages
    return result

print(solution())