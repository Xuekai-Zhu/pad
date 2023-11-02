def solution():
    cardinals = 3
    robins = cardinals * 4
    blue_jays = cardinals * 2
    sparrows = cardinals * 3 + 1
    total_birds = cardinals + robins + blue_jays + sparrows
    result = total_birds
    return result

print(solution())