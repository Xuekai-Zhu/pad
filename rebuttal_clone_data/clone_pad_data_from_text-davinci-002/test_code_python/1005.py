def solution():
    original_price = 20
    percent_discount = 50
    discount_amount = original_price * (percent_discount / 100)
    price_after_discount = original_price - discount_amount
    
    total_price = price_after_discount * 4
    result = total_price
    return result

print(solution())