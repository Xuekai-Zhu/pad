def solution():
    initial_stickers = 135
    used_stickers = initial_stickers / 3
    remaining_stickers = initial_stickers - used_stickers
    friend_stickers = remaining_stickers * (2/5)
    Oliver_stickers = remaining_stickers - friend_stickers
    result = Oliver_stickers
    return result

print(solution())