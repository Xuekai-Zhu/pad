def solution():
    space_stickers = 100
    cat_stickers = 50
    total_stickers = space_stickers + cat_stickers
    stickers_left = total_stickers % 3
    result = stickers_left
    return result

print(solution())