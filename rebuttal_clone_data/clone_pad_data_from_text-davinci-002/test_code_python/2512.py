def solution():
    eggplants = 5
    zucchini = 4
    tomatoes = 4
    onions = 3
    basil = 1
    cost_eggplants = eggplants * 2
    cost_zucchini = zucchini * 2
    cost_tomatoes = tomatoes * 3.5
    cost_onions = onions * 1
    cost_basil = basil * 2.5
    total_cost = cost_eggplants + cost_zucchini + cost_tomatoes + cost_onions + cost_basil
    cost_per_quart = total_cost / 4
    result = cost_per_quart
    
    return result

print(solution())