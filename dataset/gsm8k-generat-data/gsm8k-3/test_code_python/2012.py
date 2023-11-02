def solution():
    """Ryan has 30 stickers. Steven has thrice as many stickers as Ryan. Terry has 20 more stickers than Steven. How many stickers do they have altogether?"""
    # Define the number of stickers Ryan has
    ryan_stickers = 30

    # Calculate the number of stickers Steven has
    steven_stickers = ryan_stickers * 3

    # Calculate the number of stickers Terry has
    terry_stickers = steven_stickers + 20

    # Calculate the total number of stickers they have altogether
    total_stickers = ryan_stickers + steven_stickers + terry_stickers

    # Display the total number of stickers
    result = total_stickers
    return result

print(solution())