def solution():
    """Coral is reading a book that is 600 pages long.  She reads half of it in the first week, and 30 percent of the remaining pages the second week. How many pages must she read the third week in order to finish the book?"""
    # Define the total number of pages in the book
    total_pages = 600

    # Calculate the number of pages Coral read in the first week
    pages_read_week1 = total_pages / 2

    # Calculate the number of pages remaining after the first week
    pages_remaining = total_pages - pages_read_week1

    # Calculate the number of pages Coral read in the second week
    pages_read_week2 = pages_remaining * 0.3

    # Calculate the number of pages remaining after the second week
    pages_remaining = pages_remaining - pages_read_week2

    # Calculate the number of pages Coral must read in the third week to finish the book
    pages_to_read_week3 = pages_remaining

    # Display the number of pages Coral must read in the third week
    result = pages_to_read_week3
    return result

print(solution())