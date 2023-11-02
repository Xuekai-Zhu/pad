def solution():
    
    original_price = 50
    discount_percent = 30
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())