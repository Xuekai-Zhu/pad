def solution():
    
    
    blueberry_cost_per_ounce = 5/6
    raspberry_cost_per_ounce = 3/8
    
    total_ounces = 4 * 12
    
    blueberry_cost = blueberry_cost_per_ounce * total_ounces
    raspberry_cost = raspberry_cost_per_ounce * total_ounces
    
    money_saved = blueberry_cost - raspberry_cost
    
    result = money_saved
    return result

print(solution())