def solution():
    """Shannon bought 5 pints of frozen yogurt, two packs of chewing gum, and five trays of jumbo shrimp from The Food Place for a total of  $55 If the price of a tray of jumbo shrimp is $5 and a pack of chewing gum costs half as much as a pint of frozen yogurt, what is the price of a pint of frozen yogurt?"""
    # Define the cost of a tray of jumbo shrimp and the number of trays purchased
    SHRIMP_COST = 5
    SHRIMP_TRAYS = 5

    # Define the number of packs of chewing gum purchased
    GUM_PACKS = 2

    # Define the total cost and the number of pints of frozen yogurt purchased
    total_cost = 55
    yogurt_pints = 5

    # Calculate the cost of the jumbo shrimp
    shrimp_cost = SHRIMP_COST * SHRIMP_TRAYS

    # Calculate the cost of the chewing gum
    gum_cost = yogurt_pints / 2

    # Calculate the cost of the frozen yogurt
    yogurt_cost = total_cost - shrimp_cost - gum_cost

    # Calculate the price of a pint of frozen yogurt
    price_per_pint = yogurt_cost / yogurt_pints

    # Display the price of a pint of frozen yogurt
    result = price_per_pint
    return result

print(solution())