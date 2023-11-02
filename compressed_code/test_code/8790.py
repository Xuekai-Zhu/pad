def solution():
    
    num_fandoms = 4
    shirts_per_fandom = 5
    shirt_price = 15
    discount_percent = 20
    tax_percent = 10
    
    
    total_shirt_cost = num_fandoms * shirts_per_fandom * shirt_price
    
    
    final_shirt_cost = total_shirt_cost * (1 - (discount_percent / 100))
    
    
    total_cost = final_shirt_cost * (1 + (tax_percent / 100))
    
    result = total_cost
    return result

print(solution())