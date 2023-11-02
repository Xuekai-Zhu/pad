def solution():
    """Jerry has three times as many stickers as George. George has 6 fewer stickers than his brother Fred. If Fred has 18 stickers, how many stickers does Jerry have?"""
    
    # Define the number of stickers Fred has
    fred_stickers = 18

    # Calculate the number of stickers George has
    george_stickers = fred_stickers - 6

    # Calculate the number of stickers Jerry has
    jerry_stickers = 3 * george_stickers

    # return the number of stickers Jerry has
    result = jerry_stickers
    return result

print(solution())