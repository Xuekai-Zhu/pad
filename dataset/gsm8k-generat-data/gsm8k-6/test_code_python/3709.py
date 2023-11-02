def solution():
    # Calculate the total number of stickers June and Bonnie had before receiving new ones
    june_stickers = 76
    bonnie_stickers = 63
    total_stickers = june_stickers + bonnie_stickers

    # Add the number of stickers they received as a gift
    total_stickers += 25*2  # Each of them received 25 stickers as a gift

    result = total_stickers
    return result

print(solution())