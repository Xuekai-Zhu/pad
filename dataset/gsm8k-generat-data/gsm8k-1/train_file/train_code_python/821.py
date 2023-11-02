def solution():
    """Cupcakes are sold in packages of 10 and 15. Jean bought 4 packs of 15 cupcakes. If she will give one cupcake each to 100 children in the orphanage, how many packs of 10 cupcakes should she need to buy?"""
    packs_of_15 = 4
    cupcakes_per_pack_15 = 15
    total_cupcakes_15 = packs_of_15 * cupcakes_per_pack_15
    children = 100
    cupcakes_needed = children - total_cupcakes_15
    packs_of_10_needed = abs(cupcakes_needed) // 10
    if cupcakes_needed % 10 != 0:
        packs_of_10_needed += 1
    result = packs_of_10_needed
    return result

print(solution())