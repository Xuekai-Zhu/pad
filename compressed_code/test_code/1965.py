def solution():
    
    eggplant_price = 2.00
    zucchini_price = 2.00
    tomato_price = 3.50
    onion_price = 1.00
    basil_price = 2.50 * 2  

    eggplant_cost = eggplant_price * 5
    zucchini_cost = zucchini_price * 4
    tomato_cost = tomato_price * 4
    onion_cost = onion_price * 3
    basil_cost = basil_price * 1

    total_cost = eggplant_cost + zucchini_cost + tomato_cost + onion_cost + basil_cost
    cost_per_quart = total_cost / 4

    result = cost_per_quart
    return result

print(solution())