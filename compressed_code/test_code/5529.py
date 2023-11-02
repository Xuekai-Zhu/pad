def solution():
    
    cube_volume = 6 ** 3
    gold_density = 19
    gold_weight = cube_volume * gold_density
    gold_price = 60
    total_cost = gold_weight * gold_price
    selling_price = 1.5 * total_cost
    profit = selling_price - total_cost
    result = profit
    return result

print(solution())