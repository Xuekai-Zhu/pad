def solution():
    """Oliver had 135 stickers. He used 1/3 of his stickers, gave 2/5 of the remaining to his friend, and kept the remaining stickers. How many stickers did he keep?"""
    initial_stickers = 135
    used_stickers = initial_stickers / 3
    remaining_stickers = initial_stickers - used_stickers
    given_stickers = remaining_stickers * 2 / 5
    kept_stickers = remaining_stickers - given_stickers
    result = kept_stickers
    return result

print(solution())