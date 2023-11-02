def solution():
    """Shannon bought 5 pints of frozen yogurt, two packs of chewing gum, and five trays of jumbo shrimp from The Food Place for a total of  $55 If the price of a tray of jumbo shrimp is $5 and a pack of chewing gum costs half as much as a pint of frozen yogurt, what is the price of a pint of frozen yogurt?"""
    # Define the number of purchased items
    yogurt_pints = 5
    gum_packs = 2
    shrimp_trays = 5

    # Define the total cost
    total_cost = 55

    # Calculate the cost of jumbo shrimp
    shrimp_cost = shrimp_trays * 5

    # Calculate the cost of chewing gum
    gum_cost = yogurt_pints / 2 

    # Calculate the total cost of frozen yogurt
    yogurt_cost = total_cost - shrimp_cost - gum_cost

    # Calculate the price per pint of frozen yogurt
    yogurt_price = yogurt_cost / yogurt_pints

    result = round(yogurt_price, 2)
    return result

print(solution())