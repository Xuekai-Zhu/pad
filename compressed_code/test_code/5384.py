def solution():
    
    hamburger_price = 3.5
    hamburger_weight = 2
    buns_price = 1.5
    lettuce_price = 1
    tomato_price = 2
    tomato_weight = 1.5
    pickles_price = 2.5
    pickles_coupon = 1
    total_price = (hamburger_price * hamburger_weight) + buns_price + lettuce_price + (tomato_price * tomato_weight) + (pickles_price - pickles_coupon)
    change = 20 - total_price
    result = change
    return result

print(solution())