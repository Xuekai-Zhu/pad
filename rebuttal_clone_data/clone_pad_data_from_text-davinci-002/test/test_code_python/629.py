def solution():
    initial_stickers = 89
    large_stickers = 3
    small_stickers = 7
    pages = 6
    stickers_used = (large_stickers + (small_stickers * pages))
    remaining_stickers = initial_stickers - stickers_used
    result = remaining_stickers
    
    return result

print(solution())