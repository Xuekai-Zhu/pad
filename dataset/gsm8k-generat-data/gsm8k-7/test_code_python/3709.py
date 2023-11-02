def solution():
    june_stickers = 76
    bonnie_stickers = 63
    stickers_per_grandparent = 25

    # Calculate the new total number of stickers for June and Bonnie after the grandparents' gift
    june_stickers += stickers_per_grandparent
    bonnie_stickers += stickers_per_grandparent

    # Calculate the combined number of stickers
    total_stickers = june_stickers + bonnie_stickers
    result = total_stickers
    return result

print(solution())