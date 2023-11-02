def solution():
    
    lemon_price_increase = 4
    grape_price_increase = 0.5 * lemon_price_increase
    new_lemon_price = 8 + lemon_price_increase
    new_grape_price = 7 + grape_price_increase
    lemons = 80
    grapes = 140
    total_money = (lemons * new_lemon_price) + (grapes * new_grape_price)
    result = total_money
    return result

print(solution())