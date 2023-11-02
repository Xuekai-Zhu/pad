def solution():
    total_pages = 30  # Joey has 30 pages to read
    percentage_to_read = 0.7  # Joey wants to take a break after reading 70% of the pages

    # Calculate the number of pages Joey needs to read before taking a break
    pages_before_break = total_pages * percentage_to_read

    # Calculate the number of pages Joey needs to read after taking a break
    pages_after_break = total_pages - pages_before_break
    result = pages_after_break
    return result

print(solution())