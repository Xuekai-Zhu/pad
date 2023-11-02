def solution():
    tuna_packs = 5
    tuna_price = 2
    water_bottles = 4
    water_price = 1.5
    cost_of_tuna = tuna_packs * tuna_price
    cost_of_water = water_bottles * water_price
    total_cost = cost_of_tuna + cost_of_water
    other_goods = total_cost - 56
    result = other_goods 
    return result

print(solution())