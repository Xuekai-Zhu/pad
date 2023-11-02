def solution():
    """Clara brings a package of 100 stickers to school. She gives 10 stickers to a boy she likes. She gives half of the stickers which she has left to her best friends. How many stickers does Clara have left?"""
    initial_stickers = 100
    stickers_given = 10
    stickers_left = initial_stickers - stickers_given
    stickers_to_friends = stickers_left / 2
    total_stickers_left = stickers_left - stickers_to_friends
    result = total_stickers_left
    return result

print(solution())