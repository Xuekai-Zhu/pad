def solution():
    """Scott wants to make and freeze a large batch of ratatouille. At the farmers' market he buys 5 pounds of eggplants and 4 pounds of zucchini at $2.00 a pound. He needs 4 pounds of tomatoes that are $3.50 a pound. The onions are $1.00 a pound and he needs 3 pounds. Then he needs a pound of basil which is sold for $2.50 per half pound. If this yields 4 quarts, how much does each quart cost?"""
    # Calculate the total cost of eggplants and zucchinis
    cost_ez = (5 + 4) * 2

    # Calculate the total cost of tomatoes and onions
    cost_to = 4 * 3.5 + 3 * 1

    # Calculate the total cost of basil
    cost_ba = (2.5 / 0.5) * 1

    # Calculate the total cost of all the ingredients
    total_cost = cost_ez + cost_to + cost_ba

    # Calculate the cost per quart
    cost_per_quart = total_cost / 4

    result = cost_per_quart
    return result

print(solution())