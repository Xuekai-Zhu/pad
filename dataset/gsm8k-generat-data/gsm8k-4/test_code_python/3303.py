def solution():
    """Anahi bought a 500 pages book to write some notes on. In the first week, she wrote on 150 pages. In the second week, she wrote on 30% of the remaining pages. While continuing writing, she accidentally spilled coffee on the book and damaged 20 percent of the empty pages she was to write on. Calculate the total number of empty pages available for her to write on now."""
    # Define the total number of pages in the book
    total_pages = 500

    # Subtract the pages written in the first week
    remaining_pages = total_pages - 150

    # Calculate the pages written in the second week
    written_pages = remaining_pages * 0.3

    # Calculate the remaining empty pages
    empty_pages = remaining_pages - written_pages

    # Calculate the number of pages damaged by coffee
    coffee_damaged = empty_pages * 0.2

    # Subtract the damaged pages to get the total available pages
    available_pages = empty_pages - coffee_damaged

    # Return the result
    result = available_pages
    return result

print(solution())