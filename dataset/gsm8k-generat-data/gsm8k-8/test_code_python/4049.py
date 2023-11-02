def solution():
    total_pages = 360
    pages_read_saturday = 40 + 10
    pages_read_sunday = 2 * pages_read_saturday

    # Calculate the total pages read
    total_pages_read = pages_read_saturday + pages_read_sunday

    # Calculate the pages left to read
    pages_left = total_pages - total_pages_read
    result = pages_left
    return result

print(solution())