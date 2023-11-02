def solution():
    """Andrew bought 750 stickers. He shared some of his stickers with his friends, Daniel and Fred.  Daniel received 250 stickers, while Fred received 120 more stickers than Daniel.   He kept the remaining stickers. How many stickers did Andrew keep?"""
    # Define the number of stickers that Andrew bought and gave away
    total_stickers = 750
    daniel_stickers = 250
    fred_stickers = daniel_stickers + 120

    # Calculate the total number of stickers that Andrew gave away
    given_away = daniel_stickers + fred_stickers

    # Calculate the number of stickers that Andrew kept
    kept = total_stickers - given_away

    # Display the number of stickers that Andrew kept
    result = kept
    return result

print(solution())