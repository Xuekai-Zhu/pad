def solution():
    # Calculate the cost of buying the 16 oz package
    cost_package = 7  

    # Calculate the cost of buying an 8 oz package and 2 discounted 4 oz packages
    cost_8oz = 4  
    cost_4oz = 2 * 0.5 * 2  # 50% discount on each 4 oz package
    cost_total = cost_8oz + cost_4oz  

    # Compare the costs and return the lowest price
    result = min(cost_package, cost_total)
    return result

print(solution())