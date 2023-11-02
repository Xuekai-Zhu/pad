def solution():
    # Define the number of packages and the price per pound
    packages = 3
    price_per_pound = 4
    
    # Calculate the total weight and cost
    total_weight = packages * 2
    total_cost = total_weight * price_per_pound
    
    result = total_cost
    return result

print(solution())