def solution():
    
    tuna_price = 2
    water_price = 1.5
    tuna_packs = 5
    water_bottles = 4
    total_spent = 56
    spent_on_tuna = tuna_price * tuna_packs
    spent_on_water = water_price * water_bottles
    spent_on_other_goods = total_spent - spent_on_tuna - spent_on_water
    result = spent_on_other_goods
    return result

print(solution())