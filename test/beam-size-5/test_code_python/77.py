def solution():
    
    initial_stickers = 10
    bought_stickers = 21
    birthday_stickers = 23
    given_away_stickers = 9
    decorate_cards = 28
    remaining_stickers = initial_stickers - bought_stickers - birthday_stickers - given_away_stickers + decorate_cards
    result = remaining_stickers
    return result

print(solution())