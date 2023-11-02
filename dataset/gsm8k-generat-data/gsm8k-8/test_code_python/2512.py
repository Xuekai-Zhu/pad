def solution():
    # Calculate the cost of the eggplants and zucchini
    veggie_cost = (5 + 4) * 2

    # Calculate the cost of the tomatoes and onions
    tomato_cost = 4 * 3.5
    onion_cost = 1 * 1

    # Calculate the cost of the basil
    basil_cost = 2.5 * 2

    # Calculate the total cost
    total_cost = veggie_cost + tomato_cost + onion_cost + basil_cost

    # Calculate the cost per quart
    cost_per_quart = total_cost / 4
    result = cost_per_quart
    return result

print(solution())