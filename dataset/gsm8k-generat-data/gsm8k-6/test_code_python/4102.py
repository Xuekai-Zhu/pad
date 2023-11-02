def solution():
    # Calculate the price of each iPhone case
    price_per_unit = 500 / 18
    
    # Calculate the original price per unit
    if 18 > 15:
        original_price_per_unit = price_per_unit / 0.8
    else:
        original_price_per_unit = price_per_unit
        
    # Calculate the original price for 1 unit
    original_price = original_price_per_unit * 1
    
    result = original_price
    return result

print(solution())