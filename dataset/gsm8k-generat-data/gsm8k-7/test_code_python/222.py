def solution():
    total_pages = 408
    pages_read_weekend = 113
    days_left = 5

    # Calculate the remaining pages that Bekah needs to read
    remaining_pages = total_pages - pages_read_weekend

    # Calculate the number of pages Bekah needs to read per day to finish in 5 days
    pages_per_day = remaining_pages / days_left
    result = pages_per_day
    return result

print(solution())