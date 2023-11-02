def solution():
    marys_stickers = 1500
    susan_stickers = marys_stickers / 3
    andrew_stickers = susan_stickers
    sam_stickers = marys_stickers - susan_stickers - andrew_stickers
    andrew_stickers_after_sam_gives_him_two_thirds = andrew_stickers + (sam_stickers * 2 / 3)
    result = andrew_stickers_after_sam_gives_him_two_thirds
    return result

print(solution())