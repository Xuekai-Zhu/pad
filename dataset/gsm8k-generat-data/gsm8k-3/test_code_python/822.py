def solution():
    """Cupcakes are sold in packages of 10 and 15. Jean bought 4 packs of 15 cupcakes.  If she will give one cupcake each to 100 children in the orphanage, how many packs of 10 cupcakes should she need to buy?"""
    # Define the number of cupcakes in each pack
    PACK_10 = 10
    PACK_15 = 15

    # Define the number of packs of each size that Jean bought
    packs_15 = 4

    # Calculate the number of cupcakes that Jean has
    cupcakes = packs_15 * PACK_15

    # Calculate the number of packs of 10 cupcakes needed to give one cupcake each to 100 children
    packs_10 = (100 - cupcakes) / PACK_10

    # Round up to the nearest integer since Jean cannot buy a fraction of a pack
    packs_10 = int(-(-packs_10 // 1))

    # Display the number of packs of 10 cupcakes needed to buy
    result = packs_10
    return result

print(solution())