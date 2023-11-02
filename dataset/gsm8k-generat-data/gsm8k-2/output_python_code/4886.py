def solution():
    """Oliver had 135 stickers. He used 1/3 of his stickers, gave 2/5 of the remaining to his friend, and kept the remaining stickers. How many stickers did he keep?"""
    total_stickers = 135
    used_stickers = total_stickers * (1/3)
    remaining_stickers = total_stickers - used_stickers
    friend_stickers = remaining_stickers * (2/5)
    kept_stickers = remaining_stickers - friend_stickers
    result = kept_stickers
    return result

print(solution())