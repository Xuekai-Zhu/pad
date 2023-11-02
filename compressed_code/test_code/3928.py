def solution():
    
    original_price = 250
    discount_amount = (original_price // 100) * 10
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())