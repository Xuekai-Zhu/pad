def solution():
    """Silvia wants to buy a new guitar online. The price of the guitar has a suggested retail price of $1000. Guitar Center has a special deal of 15% off but has a shipping fee of $100. Sweetwater has a 10% off deal with free shipping. How much will she save by buying from the cheaper store compared to the other store?"""
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