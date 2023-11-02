def solution():
    """A carton contains 12 boxes. If each box has 10 packs of cheese cookies, what's the price of a pack of cheese cookies if a dozen cartons cost $1440?"""
    # Define the number of boxes and packs per box
    BOXES_PER_CARTON = 12
    PACKS_PER_BOX = 10

    # Define the total number of packs in a dozen cartons
    total_packs = BOXES_PER_CARTON * PACKS_PER_BOX * 12

    # Define the total cost of a dozen cartons
    total_cost = 1440

    # Calculate the price per pack
    price_per_pack = total_cost / total_packs

    # Display the price per pack
    result = price_per_pack
    return result

print(solution())