def solution():
    money_given = 71
    shirt_price = 5
    pants_price = 26
    money_spent = shirt_price * 5 + pants_price
    money_left = money_given - money_spent
    result = money_left
    return result

print(solution())