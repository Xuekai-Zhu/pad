def solution():
    # Calculate the total cost of Arthur's meal without the discount and tip
    total_cost = 8 + 20 + 3*2 + 6  # cost of appetizer, entrée, wine, and dessert

    # Calculate the discounted cost of Arthur's meal
    discounted_cost = (1/2) * 20  # half off the price of the entrée

    # Calculate the tip on the full cost of Arthur's meal
    tip = 0.2 * total_cost

    # Calculate the total cost of Arthur's meal including the discount and tip
    total_cost_with_tip = discounted_cost + tip + 8 + 3*2 + 6  # add the cost of the appetizer, wine, and dessert

    result = total_cost_with_tip
    return result

print(solution())