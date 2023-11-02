def solution():
    
    cheese_price = 4
    vegetable_price = cheese_price + 2
    cheese_weight = 8
    vegetable_weight = 7
    total_cheese_price = cheese_price * cheese_weight
    total_vegetable_price = vegetable_price * vegetable_weight
    total_price = total_cheese_price + total_vegetable_price
    result = total_price
    return result

print(solution())