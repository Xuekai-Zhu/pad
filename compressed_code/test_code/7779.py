def solution():
    
    eggplant_cost = 5 * 2
    zucchini_cost = 4 * 2
    tomato_cost = 4 * 3.5
    onion_cost = 3 * 1
    basil_cost = 2.5 * 2
    total_cost = eggplant_cost + zucchini_cost + tomato_cost + onion_cost + basil_cost
    cost_per_quart = total_cost / 4
    result = cost_per_quart
    return result

print(solution())