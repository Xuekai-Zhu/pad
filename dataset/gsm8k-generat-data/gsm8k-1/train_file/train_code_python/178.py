def solution():
    """Colton had 72 dolphin stickers. He gave 4 stickers each to 3 friends. He also gave his friend Mandy 2 more than he gave his three friends total. And he gave Justin 10 less than Mandy. How many stickers does Colton have left?"""
    initial_stickers = 72
    stickers_given = 4 * 3
    mandy_given = stickers_given + 2
    justin_given = mandy_given - 10
    total_given = stickers_given + mandy_given + justin_given
    stickers_left = initial_stickers - total_given
    result = stickers_left
    return result

print(solution())