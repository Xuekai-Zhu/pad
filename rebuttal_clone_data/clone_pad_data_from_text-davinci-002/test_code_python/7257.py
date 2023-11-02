def solution():
    beef_bought = 20
    pork_bought = beef_bought / 2
    total_meat = beef_bought + pork_bought
    meat_used = 1.5
    meat_leftover = total_meat - meat_used
    selling_price = 20
    money_made = selling_price * meat_leftover
    result = money_made
    
    return result

print(solution())