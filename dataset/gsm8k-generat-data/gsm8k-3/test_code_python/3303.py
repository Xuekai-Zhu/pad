def solution():
    """Anahi bought a 500 pages book to write some notes on. In the first week, she wrote on 150 pages. In the second week, she wrote on 30% of the remaining pages. While continuing writing, she accidentally spilled coffee on the book and damaged 20 percent of the empty pages she was to write on. Calculate the total number of empty pages available for her to write on now."""
    # Define the total number of pages in the book
    TOTAL_PAGES = 500

    # Define the number of pages written in the first week
    pages_written_week1 = 150

    # Calculate the number of pages remaining after the first week
    pages_remaining_week1 = TOTAL_PAGES - pages_written_week1

    # Calculate the number of pages written in the second week
    pages_written_week2 = int(0.3 * pages_remaining_week1)

    # Calculate the number of pages remaining after the second week
    pages_remaining_week2 = pages_remaining_week1 - pages_written_week2

    # Calculate the number of pages damaged by the coffee spill
    pages_damaged = int(0.2 * pages_remaining_week2)

    # Calculate the total number of empty pages available for writing
    empty_pages = pages_remaining_week2 - pages_damaged

    # Display the total number of empty pages available for writing
    result = empty_pages
    return result

print(solution())