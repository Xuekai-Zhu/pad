def solution():
    """Jerry has three times as many stickers as George. George has 6 fewer stickers than his brother Fred. If Fred has 18 stickers, how many stickers does Jerry have?"""
    fred_stickers = 18
    george_stickers = fred_stickers - 6
    jerry_stickers = 3 * george_stickers
    result = jerry_stickers
    return result

print(solution())