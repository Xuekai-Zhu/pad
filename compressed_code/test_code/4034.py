def solution():
    
    gallon_cost = 8
    gallon_size = 128  
    normal_cost_per_ounce = 3 / 16
    normal_cost_for_gallon = normal_cost_per_ounce * gallon_size
    savings = normal_cost_for_gallon - gallon_cost
    result = savings
    return result

print(solution())