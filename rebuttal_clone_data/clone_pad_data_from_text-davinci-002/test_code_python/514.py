def solution():
    initial_stickers = 100
    given_away = 10 + (initial_stickers / 2)
    result = initial_stickers - given_away
    return result

print(solution())