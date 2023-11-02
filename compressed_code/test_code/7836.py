def solution():
    
    full_price = 85
    discount_1 = 0.2
    discount_2 = 0.25
    final_price = full_price * (1 - discount_1) * (1 - discount_2)
    result = final_price
    return result

print(solution())