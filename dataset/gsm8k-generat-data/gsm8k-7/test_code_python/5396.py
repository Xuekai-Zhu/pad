def solution():
    pages_per_day = 2 * 10
    remaining_days = 6
    total_pages = 100

    # Calculate the total number of pages Justin will read in the remaining 6 days
    remaining_pages = pages_per_day * remaining_days

    # Add the pages he already read to the total pages
    total_pages_read = 10 + remaining_pages

    # Check if Justin will pass his class or not
    if total_pages_read >= total_pages:
        result = total_pages_read
    else:
        result = "Justin will not be able to pass the class."

    return result

print(solution())