def solution():
    red_stamps = 30
    white_stamps = 80
    red_price = 0.5
    white_price = 0.2
    simon_money = red_stamps * red_price
    peter_money = white_stamps * white_price
    difference = simon_money - peter_money
    result = difference
    return result

print(solution())