def solution():
    # Calculate the total number of stickers Peggy uses
    red_stickers = 3 * 10 * 3  # Each sheet in the red folder gets 3 stickers
    green_stickers = 2 * 10 * 1  # Each sheet in the green folder gets 2 stickers
    blue_stickers = 1 * 10 * 1  # Each sheet in the blue folder gets 1 sticker
    total_stickers = red_stickers + green_stickers + blue_stickers  # Total number of stickers used
    result = total_stickers
    return result

print(solution())