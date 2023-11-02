def solution():
    """Ryan has 30 stickers. Steven has thrice as many stickers as Ryan. Terry has 20 more stickers than Steven. How many stickers do they have altogether?"""
    ryan_stickers = 30
    steven_stickers = 3 * ryan_stickers
    terry_stickers = steven_stickers + 20
    total_stickers = ryan_stickers + steven_stickers + terry_stickers
    result = total_stickers
    return result

print(solution())