def solution():
    # Calculate the total square footage of the deck
    total_sq_ft = 30 * 40

    # Calculate the cost of the deck without sealant
    deck_cost = total_sq_ft * 3

    # Calculate the cost of the sealant
    sealant_cost = total_sq_ft * 1

    # Calculate the total cost
    total_cost = deck_cost + sealant_cost
    result = total_cost
    return result

print(solution())