def solution():
    
    initial_stickers = 135
    used_stickers = initial_stickers / 3
    remaining_stickers = initial_stickers - used_stickers
    given_stickers = remaining_stickers * 2 / 5
    kept_stickers = remaining_stickers - given_stickers
    result = kept_stickers
    return result

print(solution())