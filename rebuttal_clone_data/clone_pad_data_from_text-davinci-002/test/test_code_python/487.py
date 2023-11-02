def solution():
    money_initial = 30
    money_spent1 = 10
    money_left = money_initial - money_spent1
    money_spent2 = money_left / 4
    money_final = money_left - money_spent2
    result = money_final
    return result

print(solution())