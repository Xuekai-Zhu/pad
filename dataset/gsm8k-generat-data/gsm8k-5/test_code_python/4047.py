def solution():
    # Calculate the cost of the skirts
    skirt_cost = 3 * 20  # Marcia needs 3 skirts, each costs $20

    # Calculate the cost of the blouses
    blouse_cost = 5 * 15  # Marcia needs 5 blouses, each costs $15

    # Calculate the cost of the pants
    pant_cost = 2 * 30 + 30/2  # Marcia needs 2 pairs of pants, each costs $30, and she gets 1/2 off on the second pair

    # Calculate the total cost of her wardrobe
    total_cost = skirt_cost + blouse_cost + pant_cost
    result = total_cost
    return result

print(solution())