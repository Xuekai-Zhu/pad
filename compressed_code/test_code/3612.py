def solution():
    
    total_money = 343
    each_brother_money = (1/7) * total_money
    money_left = total_money - (2 * each_brother_money)
    result = money_left
    return result

print(solution())