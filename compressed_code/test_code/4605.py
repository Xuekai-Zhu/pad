def solution():
    
    distance = 150 * 2  
    gas_price_per_liter = 0.9
    gas_km_per_liter = 15
    gas_needed = distance / gas_km_per_liter
    gas_price_total = gas_price_per_liter * gas_needed
    option1_price = 50 + gas_price_total
    option2_price = 90
    savings = option2_price - option1_price
    result = savings
    return result

print(solution())