def solution():
    
    original_price = 60 / 3  
    discount_percentage = 40
    discounted_price = original_price * (1 - discount_percentage/100)
    result = discounted_price
    return result

print(solution())