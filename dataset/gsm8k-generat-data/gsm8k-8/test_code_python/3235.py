def solution():
    # Define total number of pages and pages read on Saturday and Sunday
    total_pages = 93
    pages_read_saturday = 30
    pages_read_sunday = 20

    # Calculate remaining pages
    remaining_pages = total_pages - (pages_read_saturday + pages_read_sunday)
    result = remaining_pages
    return result

print(solution())