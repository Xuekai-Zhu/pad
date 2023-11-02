def solution():
    """Scott wants to make and freeze a large batch of ratatouille. At the farmers' market he buys 5 pounds of eggplants and 4 pounds of zucchini at $2.00 a pound. He needs 4 pounds of tomatoes that are $3.50 a pound. The onions are $1.00 a pound and he needs 3 pounds. Then he needs a pound of basil which is sold for $2.50 per half pound. If this yields 4 quarts, how much does each quart cost?"""
    eggplant_price = 2.00
    zucchini_price = 2.00
    tomato_price = 3.50
    onion_price = 1.00
    basil_price = 2.50 * 2  # since a pound of basil is sold for $2.50 per half pound

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