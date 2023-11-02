def solution():
    """Colton had 72 dolphin stickers. He gave 4 stickers each to 3 friends. He also gave his friend Mandy 2 more than he gave his three friends total.  And he gave Justin 10 less than Mandy. How many stickers does Colton have left?"""
    original_stickers = 72
    stickers_given = 3 * 4
    given_to_mandy = stickers_given + 2
    given_to_justin = given_to_mandy - 10
    total_given = stickers_given + given_to_mandy + given_to_justin
    result = original_stickers - total_given
    return result

print(solution())