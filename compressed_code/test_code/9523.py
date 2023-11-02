def solution():
    
    money_left = 15
    doris_spent = 6
    martha_spent = doris_spent / 2
    total_spent = doris_spent + martha_spent
    initial_money = money_left + total_spent
    result = initial_money
    return result

print(solution())