def solution():
    original_price = 800
    discount_percent = 15
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    result = final_price
    
    return result

print(solution())