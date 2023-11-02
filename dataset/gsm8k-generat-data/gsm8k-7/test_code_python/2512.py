def solution():
    eggplant_amount = 5
    eggplant_price = 2.0

    zucchini_amount = 4
    zucchini_price = 2.0

    tomato_amount = 4
    tomato_price = 3.5

    onion_amount = 3
    onion_price = 1.0

    basil_amount = 1  # 1 pound is equal to 2 half pounds
    basil_price = 2.5 / 2

    total_weight = eggplant_amount + zucchini_amount + tomato_amount + onion_amount + basil_amount
    total_cost = (eggplant_amount + zucchini_amount) * eggplant_price + tomato_amount * tomato_price + onion_amount * onion_price + basil_amount * basil_price

    cost_per_quart = total_cost / 4
    result = cost_per_quart
    return result

print(solution())