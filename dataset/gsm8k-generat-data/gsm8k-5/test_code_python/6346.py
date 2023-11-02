def solution():
    days_read = 12 - 1  # Bill read for 11 days
    pages_per_day = 8  # Bill reads 8 pages per day
    fraction_covered = 2 / 3  # Bill covered 2/3 of the book

    # Calculate the total number of pages in the book
    total_pages = (days_read * pages_per_day) / fraction_covered
    result = total_pages
    return result

print(solution())