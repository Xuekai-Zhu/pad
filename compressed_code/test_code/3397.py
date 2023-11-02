def solution():
    
    apple_price = 2
    sugar_price = apple_price - 1
    walnut_price = 6
    apple_weight = 5
    sugar_packs = 3
    walnut_weight = 0.5
    apple_cost = apple_weight * apple_price
    sugar_cost = sugar_packs * sugar_price
    walnut_cost = walnut_weight * walnut_price
    total_cost = apple_cost + sugar_cost + walnut_cost
    result = total_cost
    return result

print(solution())