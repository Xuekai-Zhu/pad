def solution():
    # Calculate the total number of days Jenna has to read
    total_days = 30 - 4 - 1  # Jenna will be busy for 4 weekdays and will read 100 pages on the 23rd

    # Calculate the total number of pages Jenna needs to read
    target_pages = 600
    total_pages_to_read = target_pages - 100

    # Calculate the number of pages Jenna needs to read per day
    pages_per_day = total_pages_to_read / total_days
    result = pages_per_day
    return result

print(solution())