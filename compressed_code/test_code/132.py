def solution():
    
    starting_stickers = 72
    friends_stickers = 4 * 3
    mandy_stickers = friends_stickers + 2
    justin_stickers = mandy_stickers - 10
    total_given_away = friends_stickers + mandy_stickers + justin_stickers
    remaining_stickers = starting_stickers - total_given_away
    result = remaining_stickers
    return result

print(solution())