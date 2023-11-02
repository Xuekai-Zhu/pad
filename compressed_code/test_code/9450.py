def solution():
    
    total_money = 343
    money_per_brother = (1/7) * total_money
    money_left = total_money - (2 * money_per_brother)
    result = money_left
    return result

print(solution())