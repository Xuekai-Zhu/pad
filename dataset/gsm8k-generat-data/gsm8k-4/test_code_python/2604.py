def solution():
    """Andrew bought 750 stickers. He shared some of his stickers with his friends, Daniel and Fred. Daniel received 250 stickers, while Fred received 120 more stickers than Daniel. He kept the remaining stickers. How many stickers did Andrew keep?"""
    # Define the total number of stickers Andrew bought
    total_stickers = 750

    # Define the number of stickers Daniel received
    daniel_stickers = 250

    # Define the number of stickers Fred received
    fred_stickers = daniel_stickers + 120

    # Calculate the total number of stickers given to Daniel and Fred
    given_stickers = daniel_stickers + fred_stickers

    # Calculate the number of stickers Andrew kept
    kept_stickers = total_stickers - given_stickers

    result = kept_stickers
    return result

print(solution())