def solution():
    """Cupcakes are sold in packages of 10 and 15. Jean bought 4 packs of 15 cupcakes.  If she will give one cupcake each to 100 children in the orphanage, how many packs of 10 cupcakes should she need to buy?"""
    # Calculate the total number of cupcakes that Jean has bought
    cupcakes_bought = 4 * 15

    # Calculate the number of cupcakes that will be given to the children
    cupcakes_given = 100

    # Calculate the remaining number of cupcakes that Jean has after giving to the children
    cupcakes_remaining = cupcakes_bought - cupcakes_given

    # Calculate the number of packs of 10 cupcakes that Jean needs to buy
    packs_of_10 = cupcakes_remaining // 10

    result = packs_of_10
    return result

print(solution())