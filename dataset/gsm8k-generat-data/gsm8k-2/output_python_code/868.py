def solution():
    """Paige bought some new stickers and wanted to share them with 3 of her friends. She decided to share a sheet of 100 space stickers and a sheet of 50 cat stickers equally among her 3 friends. How many stickers will she have left?"""
    space_stickers = 100
    cat_stickers = 50
    total_friends = 3
    stickers_per_friend = (space_stickers + cat_stickers) / total_friends
    left_over = (space_stickers + cat_stickers) % total_friends
    result = left_over
    return result

print(solution())