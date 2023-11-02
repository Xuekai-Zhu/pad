def solution():
    
    tip = 99
    steak_price = 24
    burger_price = 3.5
    ice_cream_price = 2
    total_spent = (2 * steak_price) + (2 * burger_price) + (3 * ice_cream_price)
    money_left = tip - total_spent
    result = money_left
    return result

print(solution())