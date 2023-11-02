def solution():
    """ Todd bought a pair of jeans that cost $125 at full price. The jeans were on sale for 20% off. He then applied a coupon that took off $10. He paid with a store credit card that gave him another 10% off the remaining amount. How many dollars did he save on the original price of the jeans?"""
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