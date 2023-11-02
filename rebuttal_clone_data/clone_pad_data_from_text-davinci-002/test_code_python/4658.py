def solution():
    money_given = 343
    money_shared = money_given * (1/7)
    money_left = money_given - money_shared
    result = money_left
    return result

print(solution())