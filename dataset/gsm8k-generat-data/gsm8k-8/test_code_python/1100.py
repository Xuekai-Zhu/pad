def solution():
    total_stickers = 89
    used_stickers = 3 + 6*7   # 3 for front page, and 7 for each of the 6 other pages
    remaining_stickers = total_stickers - used_stickers
    result = remaining_stickers
    return result

print(solution())