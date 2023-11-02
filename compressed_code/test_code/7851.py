def solution():
    
    total_stickers = 750
    daniel_stickers = 250
    fred_stickers = daniel_stickers + 120
    stickers_given_away = daniel_stickers + fred_stickers
    stickers_left = total_stickers - stickers_given_away
    result = stickers_left
    return result

print(solution())