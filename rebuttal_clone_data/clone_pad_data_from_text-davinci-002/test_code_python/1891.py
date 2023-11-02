def solution():
    initial_sheets = 5
    stickers_per_sheet = 10
    stickers_given_away = 100
    stickers_left = initial_sheets * stickers_per_sheet - stickers_given_away
    result = stickers_left
    return result

print(solution())