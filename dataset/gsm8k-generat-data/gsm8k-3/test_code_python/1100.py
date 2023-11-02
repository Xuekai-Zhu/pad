def solution():
    """Mary had 89 stickers.  She used 3 large stickers on the front page of her journal and 7 stickers each to 6 other pages of her journal. How many stickers does Mary have remaining?"""
    # Define the initial number of stickers
    initial_stickers = 89

    # Calculate the number of stickers used on the front page
    front_page_stickers = 3

    # Calculate the number of stickers used on other pages
    other_page_stickers = 7 * 6

    # Calculate the total number of stickers used
    total_stickers_used = front_page_stickers + other_page_stickers

    # Calculate the number of stickers remaining
    stickers_remaining = initial_stickers - total_stickers_used

    # Display the number of stickers remaining
    result = stickers_remaining
    return result

print(solution())