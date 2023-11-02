def solution():
    
    lemon_price_increase = 4
    grape_price_increase = lemon_price_increase / 2
    lemon_price_new = 8 + lemon_price_increase
    grape_price_new = 7 + grape_price_increase
    lemons = 80
    grapes = 140
    total_money_collected = (lemons * lemon_price_new) + (grapes * grape_price_new)
    result = total_money_collected
    return result

print(solution())