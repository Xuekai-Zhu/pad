def solution():
    
    regular_price = 50
    discount_percent = 20
    discounted_price = regular_price - (regular_price * (discount_percent / 100))
    shirts_per_dozen = 12
    shirts_to_buy = shirts_per_dozen / 2
    total_price = discounted_price * shirts_to_buy
    result = total_price
    return result

print(solution())