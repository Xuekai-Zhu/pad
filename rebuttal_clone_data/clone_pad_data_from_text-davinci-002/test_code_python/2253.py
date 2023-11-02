def solution():
    money = 20
    price_per_pound = 2
    pounds_bought = 3
    total_spent = price_per_pound * pounds_bought
    money_left = money - total_spent
    result = money_left
    return result

print(solution())