def solution():
    
    budget = 200
    total_cost = 42 + 18 + 14  
    helium_budget = budget - total_cost
    helium_price_per_ounce = 1.5
    helium_total_ounces = helium_budget / helium_price_per_ounce
    additional_height_per_ounce = 113
    total_additional_height = helium_total_ounces * additional_height_per_ounce
    result = total_additional_height
    return result

print(solution())