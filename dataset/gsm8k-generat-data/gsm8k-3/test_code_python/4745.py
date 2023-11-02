def solution():
    """Jerry has three times as many stickers as George. George has 6 fewer stickers than his brother Fred. If Fred has 18 stickers, how many stickers does Jerry have?"""
    # Number of stickers Fred has
    fred_stickers = 18

    # Number of stickers George has
    george_stickers = fred_stickers - 6

    # Number of stickers Jerry has
    jerry_stickers = george_stickers * 3

    # Display how many stickers Jerry has
    result = jerry_stickers
    return result

print(solution())