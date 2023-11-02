def solution():
    # Calculate the total cost of the deck with sealant
    deck_area = 30 * 40  # area of the deck
    deck_cost = deck_area * 3  # cost of the deck without sealant
    deck_cost_with_sealant = deck_cost + deck_area  # cost of the deck with sealant
    result = deck_cost_with_sealant
    return result

print(solution())