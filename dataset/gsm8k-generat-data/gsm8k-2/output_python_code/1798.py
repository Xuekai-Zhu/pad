def solution():
    """Silvia wants to buy a new guitar online. The price of the guitar has a suggested retail price of $1000. Guitar Center has a special deal of 15% off but has a shipping fee of $100. Sweetwater has a 10% off deal with free shipping. How much will she save by buying from the cheaper store compared to the other store?"""
    
    guitar_price = 1000
    
    # Guitar Center
    gc_discount = guitar_price * 0.15
    gc_shipping = 100
    gc_total_price = guitar_price - gc_discount + gc_shipping
    
    # Sweetwater
    sw_discount = guitar_price * 0.10
    sw_total_price = guitar_price - sw_discount
    
    savings = gc_total_price - sw_total_price
    
    result = savings
    return result

print(solution())