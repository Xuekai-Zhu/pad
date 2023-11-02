def solution():
    # Calculate the cost of the skirts
    skirt_cost = 3 * 20

    # Calculate the cost of the blouses
    blouse_cost = 5 * 15

    # Calculate the cost of one pair of pants
    one_pair_pants_cost = 30

    # Calculate the cost of two pairs of pants at regular price
    two_pairs_pants_cost = 2 * one_pair_pants_cost

    # Calculate the cost of one pair of pants at half price
    half_price_pants_cost = 0.5 * one_pair_pants_cost

    # Calculate the cost of the second pair of pants at half price
    second_half_price_pants_cost = 0.5 * one_pair_pants_cost

    # Calculate the total cost of the pants after the sale
    pants_cost = half_price_pants_cost + second_half_price_pants_cost

    # Calculate the total cost of the wardrobe
    total_cost = skirt_cost + blouse_cost + pants_cost
    result = total_cost
    return result

print(solution())