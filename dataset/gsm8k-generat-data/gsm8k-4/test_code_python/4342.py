def solution():
    """There are 20 stickers on a page. If you have 12 pages of stickers but lose one of the pages, then how many stickers would you have?"""
    # Define the number of stickers per page and the initial number of pages
    STICKERS_PER_PAGE = 20
    INITIAL_PAGES = 12

    # Subtract one page from the initial number of pages
    remaining_pages = INITIAL_PAGES - 1

    # Calculate the total number of stickers remaining
    total_stickers = remaining_pages * STICKERS_PER_PAGE

    # Return the result
    result = total_stickers
    return result

print(solution())