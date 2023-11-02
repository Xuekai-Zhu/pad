def solution():
    
    total_cost = 340
    shirt_price_ratio = 3/4
    shoe_price_difference = 10
    
    
    x = (total_cost - shoe_price_difference) / (1 + shirt_price_ratio + 1)
    result = x
    return result

print(solution())