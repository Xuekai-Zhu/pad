def solution():
    """If you buy 2 packs of 500 mL milk, it will cost $2.50. If you buy them individually, they will cost $1.30 each. How much is your total savings from buying ten sets of 2 packs of 500 mL milk?"""
    # Define the cost of 2 packs versus buying individually
    PACK_COST = 2.5
    INDIVIDUAL_COST = 1.3

    # Calculate the cost savings per set of 2 packs
    savings_per_set = (2 * INDIVIDUAL_COST) - PACK_COST

    # Calculate the total savings from buying ten sets of 2 packs
    total_savings = savings_per_set * 10

    # Display the total savings
    result = total_savings
    return result

print(solution())