def solution():
    cost_per_patch = 1.25
    sale_per_patch = 12.00
    number_of_patches = 100
    total_cost = cost_per_patch * number_of_patches
    total_sale = sale_per_patch * number_of_patches
    profit = total_sale - total_cost
    result = profit
    
    return result

print(solution())