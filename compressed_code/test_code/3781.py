def solution():
    
    total_stickers = 135
    used_stickers = total_stickers * (1/3)
    remaining_stickers = total_stickers - used_stickers
    friend_stickers = remaining_stickers * (2/5)
    kept_stickers = remaining_stickers - friend_stickers
    result = kept_stickers
    return result

print(solution())