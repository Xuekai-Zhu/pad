def solution():
    """Mark constructed a deck that was 30 feet by 40 feet. It cost $3 per square foot. He then paid an extra $1 per square foot for sealant. How much did he pay?"""
    # Define the dimensions of the deck
    width = 30
    length = 40

    # Calculate the area of the deck
    area = width * length

    # Calculate the cost of the deck without sealant
    deck_cost = area * 3

    # Calculate the cost of the sealant
    sealant_cost = area * 1

    # Calculate the total cost
    total_cost = deck_cost + sealant_cost

    # Return the result
    result = total_cost
    return result

print(solution())