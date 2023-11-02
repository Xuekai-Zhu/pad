def solution():
    """Coral is reading a book that is 600 pages long. She reads half of it in the first week, and 30 percent of the remaining pages the second week. How many pages must she read the third week in order to finish the book?"""
    # Define the total number of pages
    total_pages = 600

    # Calculate the number of pages read in the first week
    first_week_pages = total_pages / 2

    # Calculate the number of remaining pages
    remaining_pages = total_pages - first_week_pages

    # Calculate the number of pages read in the second week
    second_week_pages = remaining_pages * 0.3

    # Calculate the number of pages left to read
    remaining_pages = total_pages - first_week_pages - second_week_pages

    # Return the number of pages she needs to read in the third week
    result = remaining_pages
    return result

print(solution())