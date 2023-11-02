def solution():
    """If you buy 2 packs of 500 mL milk, it will cost $2.50. If you buy them individually, they will cost $1.30 each. How much is your total savings from buying ten sets of 2 packs of 500 mL milk?"""
    # Define the prices of 2 packs and individual packs
    PACK_PRICE = 2.5
    INDIVIDUAL_PRICE = 1.3

    # Calculate the cost and savings of buying 2 packs
    cost_2packs = PACK_PRICE * 10
    cost_individual = 20 * INDIVIDUAL_PRICE
    savings = cost_individual - cost_2packs

    # Return the savings
    result = savings
    return result

print(solution())