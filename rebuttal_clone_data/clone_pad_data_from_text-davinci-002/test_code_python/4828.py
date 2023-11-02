def solution():
    initial_money = 20
    money_spent = initial_money * (1/5 + 3/4)
    money_left = initial_money - money_spent
    result = money_left
    return result

print(solution())