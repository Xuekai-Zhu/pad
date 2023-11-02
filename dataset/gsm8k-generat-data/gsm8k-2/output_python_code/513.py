def solution():
    """Clara brings a package of 100 stickers to school. She gives 10 stickers to a boy she likes. She gives half of the stickers which she has left to her best friends. How many stickers does Clara have left?"""
    total_stickers = 100
    stickers_given = 10
    stickers_left = total_stickers - stickers_given
    stickers_left /= 2
    result = stickers_left
    return result

print(solution())