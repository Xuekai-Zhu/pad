def solution():
    money = 204
    money_spent = money / 2
    money_left = money - money_spent
    money_spent = money_left / 2
    money_left = money - money_spent
    result = money_left
    return result

print(solution())