def solution():
    """Colton had 72 dolphin stickers. He gave 4 stickers each to 3 friends. He also gave his friend Mandy 2 more than he gave his three friends total. And he gave Justin 10 less than Mandy. How many stickers does Colton have left?"""
    starting_stickers = 72
    friends_stickers = 4 * 3
    mandy_stickers = friends_stickers + 2
    justin_stickers = mandy_stickers - 10
    total_given_away = friends_stickers + mandy_stickers + justin_stickers
    remaining_stickers = starting_stickers - total_given_away
    result = remaining_stickers
    return result

print(solution())