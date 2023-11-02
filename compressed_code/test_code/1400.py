def solution():
    
    
    guitar_price = 1000
    
    
    gc_discount = guitar_price * 0.15
    gc_shipping = 100
    gc_total_price = guitar_price - gc_discount + gc_shipping
    
    
    sw_discount = guitar_price * 0.10
    sw_total_price = guitar_price - sw_discount
    
    savings = gc_total_price - sw_total_price
    
    result = savings
    return result

print(solution())