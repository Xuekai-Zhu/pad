def solution():
    deck_length = 30
    deck_width = 40
    cost_per_square_foot = 3
    sealant_cost_per_square_foot = 1

    # Calculate the area of the deck in square feet
    deck_area = deck_length * deck_width

    # Calculate the cost of the deck without sealant
    cost_without_sealant = deck_area * cost_per_square_foot

    # Calculate the cost of the sealant
    sealant_cost = deck_area * sealant_cost_per_square_foot

    # Calculate the total cost of the deck with sealant
    total_cost = cost_without_sealant + sealant_cost

    result = total_cost
    return result

print(solution())