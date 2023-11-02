def solution():
    
    original_price = 125
    discount_1 = 0.10
    discount_2 = 0.04
    num_children = 4
    
    
    discounted_price = original_price * (1 - discount_1)
    
    
    if num_children >= 3:
        discounted_price *= (1 - discount_2)
        
    result = discounted_price
    return result

print(solution())