def solution():
    total_pages_to_read = 100  # Justin needs to read at least 100 pages to pass his class
    pages_read_first_day = 10  # Justin read 10 pages on the first day
    days_remaining = 6  # Justin has 6 more days to read

    # Calculate the total number of pages Justin will read in the remaining 6 days
    pages_remaining = total_pages_to_read - pages_read_first_day
    pages_remaining_per_day = pages_remaining / 6
    pages_read_per_day = pages_remaining_per_day / 2  # Justin reads twice as much as the first day

    # Calculate the total number of pages Justin will read in the entire week
    total_pages_read = pages_read_first_day + (pages_read_per_day * 6)
    result = total_pages_read
    return result

print(solution())