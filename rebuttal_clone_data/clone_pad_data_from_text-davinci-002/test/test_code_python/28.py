def solution():
    
    
    money_earned = 28
    money_spent = money_earned / 7
    money_saved = (money_earned - money_spent) / 2
    money_left = money_earned - money_spent - money_saved
    money_lost = money_left - 1
    result = money_lost
    
    return result

print(solution())