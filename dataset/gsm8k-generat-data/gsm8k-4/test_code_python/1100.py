def solution():
    """Mary had 89 stickers. She used 3 large stickers on the front page of her journal and 7 stickers each to 6 other pages of her journal. How many stickers does Mary have remaining?"""
    # Define the initial number of stickers
    initial_stickers = 89

    # Define the number of stickers used on the front page
    front_page_stickers = 3

    # Define the number of pages with 7 stickers each
    other_pages = 6
    other_pages_stickers = other_pages * 7

    # Calculate the total number of stickers used
    total_stickers_used = front_page_stickers + other_pages_stickers

    # Calculate the remaining number of stickers
    remaining_stickers = initial_stickers - total_stickers_used

    # Return the result
    result = remaining_stickers
    return result

print(solution())