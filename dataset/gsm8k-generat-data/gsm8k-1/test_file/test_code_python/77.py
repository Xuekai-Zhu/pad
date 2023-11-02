def solution():
    """Charlie had 10 stickers. He bought 21 stickers from a store in the mall and got 23 stickers for his birthday.
    Then Charlie gave 9 of the stickers to his sister and used 28 to decorate a greeting card. How many stickers does Charlie have left?"""
    initial_stickers = 10
    store_stickers = 21
    birthday_stickers = 23
    given_away_stickers = 9
    used_stickers = 28
    total_stickers = initial_stickers + store_stickers + birthday_stickers - given_away_stickers - used_stickers
    result = total_stickers
    return result

print(solution())