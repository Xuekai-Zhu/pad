def solution():
    """There are 20 stickers on a page. If you have 12 pages of stickers but lose one of the pages, then how many stickers would you have?"""
    # Define the number of stickers and pages
    STICKERS_PER_PAGE = 20
    NUMBER_OF_PAGES = 12

    # Calculate the total number of stickers
    total_stickers = STICKERS_PER_PAGE * NUMBER_OF_PAGES

    # Calculate the number of stickers after losing one page
    remaining_stickers = total_stickers - STICKERS_PER_PAGE

    # Display the remaining number of stickers
    result = remaining_stickers
    return result

print(solution())