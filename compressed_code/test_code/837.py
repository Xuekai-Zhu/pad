def solution():
    
    total_stickers = 89
    large_stickers_used = 3
    page_stickers_used = 7 * 6
    remaining_stickers = total_stickers - large_stickers_used - page_stickers_used
    result = remaining_stickers
    return result

print(solution())