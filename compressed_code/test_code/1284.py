def solution():
    
    fence_length = 25  
    tree_width = 1.5  
    sale_price = 8.00
    feet_per_yard = 3
    trees_needed = fence_length * feet_per_yard / tree_width
    total_cost = trees_needed * sale_price
    result = total_cost
    return result

print(solution())