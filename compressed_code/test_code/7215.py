def solution():
    
    retail_price = 1000
    discount_gc = 0.15
    shipping_gc = 100
    price_gc = retail_price - (retail_price * discount_gc) + shipping_gc
    discount_sw = 0.10
    price_sw = retail_price - (retail_price * discount_sw)
    
    savings = price_gc - price_sw
    result = savings
    return result

print(solution())