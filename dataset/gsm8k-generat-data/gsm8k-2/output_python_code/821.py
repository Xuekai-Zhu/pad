def solution():
    """Cupcakes are sold in packages of 10 and 15. Jean bought 4 packs of 15 cupcakes. If she will give one cupcake each to 100 children in the orphanage, how many packs of 10 cupcakes should she need to buy?"""
    total_cupcakes = 4 * 15
    remaining_cupcakes = total_cupcakes - 100
    packs_of_10_needed = remaining_cupcakes // 10
    if remaining_cupcakes % 10 != 0:
        packs_of_10_needed += 1
        
    result = packs_of_10_needed
    return result

print(solution())