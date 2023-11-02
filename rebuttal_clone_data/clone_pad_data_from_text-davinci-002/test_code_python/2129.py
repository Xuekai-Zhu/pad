def solution():
    chickens = 5
    money_from_chickens = chickens * 8
    ducks_sold = (180 - money_from_chickens) / 10
    result = ducks_sold
    return result

print(solution())