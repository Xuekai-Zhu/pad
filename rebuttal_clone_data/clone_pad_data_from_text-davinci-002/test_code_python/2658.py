def solution():
    total_stickers = 100
    andrew_stickers = total_stickers / 5
    bill_stickers = (total_stickers - andrew_stickers) * 3 / 10
    given_away = andrew_stickers + bill_stickers
    result = given_away
    return result

print(solution())