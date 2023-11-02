def solution():
    total_pages = 408  # Bekah has to read 408 pages
    pages_read = 113  # Bekah has already read 113 pages
    days_left = 5  # Bekah has 5 days left to complete her assignment

    # Calculate the remaining pages Bekah needs to read
    remaining_pages = total_pages - pages_read

    # Calculate the number of pages Bekah needs to read each day
    pages_per_day = remaining_pages / days_left
    result = pages_per_day
    return result

print(solution())