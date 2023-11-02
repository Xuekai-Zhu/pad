def solution():
    
    fence_length = 25 
    tree_width = 1.5 
    tree_cost = 8 
    feet_per_yard = 3
    trees_needed = round(fence_length * feet_per_yard / tree_width)
    total_cost = trees_needed * tree_cost
    result = total_cost
    return result

print(solution())