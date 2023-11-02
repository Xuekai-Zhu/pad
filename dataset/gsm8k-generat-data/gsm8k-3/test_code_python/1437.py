def solution():
    """Mark constructed a deck that was 30 feet by 40 feet.  It cost $3 per square foot.  He then paid an extra $1 per square foot for sealant.  How much did he pay?"""
    # Calculate the area of the deck
    deck_area = 30 * 40

    # Calculate the cost of the deck without sealant
    deck_cost = deck_area * 3

    # Calculate the cost of the sealant
    sealant_cost = deck_area * 1

    # Calculate the total cost
    total_cost = deck_cost + sealant_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())