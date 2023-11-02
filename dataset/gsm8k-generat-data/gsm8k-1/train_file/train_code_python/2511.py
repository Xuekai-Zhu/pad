def solution():
    """Scott wants to make and freeze a large batch of ratatouille. At the farmers' market 
    he buys 5 pounds of eggplants and 4 pounds of zucchini at $2.00 a pound. He needs 4 pounds 
    of tomatoes that are $3.50 a pound. The onions are $1.00 a pound and he needs 3 pounds. 
    Then he needs a pound of basil which is sold for $2.50 per half pound. If this yields 
    4 quarts, how much does each quart cost?"""
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