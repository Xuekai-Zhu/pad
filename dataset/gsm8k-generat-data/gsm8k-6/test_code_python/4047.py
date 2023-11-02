def solution():
    # Calculate the total cost of the skirts
    cost_skirts = 3 * 20  # 3 skirts at $20 each

    # Calculate the total cost of the blouses
    cost_blouses = 5 * 15  # 5 blouses at $15 each

    # Calculate the total cost of the pants
    cost_pants = 2 * 30 - (1/2 * 30)  # 2 pairs of pants at $30 each, with half off for one pair

    # Calculate the total cost of the wardrobe
    total_cost = cost_skirts + cost_blouses + cost_pants
    
    result = total_cost
    return result

print(solution())