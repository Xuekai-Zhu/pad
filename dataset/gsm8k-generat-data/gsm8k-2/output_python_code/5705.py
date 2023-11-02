def solution():
    """Peggy buys 3 folders, one each in the colors red, green, and blue. She puts ten sheets of paper in each folder, and then, she puts star-shaped stickers on each sheet of paper. In the red folder, each sheet of paper gets 3 stickers. In the green folder, each sheet of paper gets 2 stickers, and in the blue folder, each sheet gets 1 sticker. What is the total number of stickers Peggy uses?"""
    red_stickers = 3 * 10
    green_stickers = 2 * 10
    blue_stickers = 1 * 10
    total_stickers = red_stickers + green_stickers + blue_stickers
    result = total_stickers
    return result

print(solution())