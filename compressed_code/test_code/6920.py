def solution():
    
    original_price = 125
    sale_percent = 20
    coupon_amount = 10
    credit_card_percent = 10
    
    sale_price = original_price * (1 - (sale_percent / 100))
    sale_price -= coupon_amount
    sale_price *= (1 - (credit_card_percent / 100))
    
    saved_amount = original_price - sale_price
    result = saved_amount
    
    return result

print(solution())