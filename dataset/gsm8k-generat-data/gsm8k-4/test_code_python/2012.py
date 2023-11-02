def solution():
    """Ryan has 30 stickers. Steven has thrice as many stickers as Ryan. Terry has 20 more stickers than Steven. How many stickers do they have altogether?"""
    # Define the initial number of stickers for Ryan
    ryan_stickers = 30

    # Calculate the number of stickers for Steven
    steven_stickers = ryan_stickers * 3

    # Calculate the number of stickers for Terry
    terry_stickers = steven_stickers + 20

    # Calculate the total number of stickers
    total_stickers = ryan_stickers + steven_stickers + terry_stickers

    # return the result
    result = total_stickers
    return result

print(solution())