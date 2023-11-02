def solution():
    """Mary had 89 stickers. She used 3 large stickers on the front page of her journal and 7 stickers each to 6 other pages of her journal. How many stickers does Mary have remaining?"""
    total_stickers = 89
    large_stickers_used = 3
    page_stickers_used = 7 * 6
    remaining_stickers = total_stickers - large_stickers_used - page_stickers_used
    result = remaining_stickers
    return result

print(solution())