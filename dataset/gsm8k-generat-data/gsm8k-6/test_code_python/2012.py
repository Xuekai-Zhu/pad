def solution():
    # Calculate the number of stickers each person has
    ryan_stickers = 30
    steven_stickers = 3 * ryan_stickers  # Steven has thrice as many stickers as Ryan
    terry_stickers = steven_stickers + 20  # Terry has 20 more stickers than Steven

    # Calculate the total number of stickers they have altogether
    total_stickers = ryan_stickers + steven_stickers + terry_stickers
    result = total_stickers
    return result

print(solution())