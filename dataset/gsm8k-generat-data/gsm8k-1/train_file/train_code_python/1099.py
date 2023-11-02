def solution():
    """Mary had 89 stickers. She used 3 large stickers on the front page of her journal and 7 stickers each to 6 other pages of her journal. How many stickers does Mary have remaining?"""
    total_stickers = 89
    stickers_used = 3 + (7*6)
    stickers_remaining = total_stickers - stickers_used
    result = stickers_remaining
    return result

print(solution())