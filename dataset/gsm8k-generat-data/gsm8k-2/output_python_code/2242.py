def solution():
    """Ginger owns a flower shop, where she sells roses, lilacs, and gardenias. On Tuesday, she sold three times more roses than lilacs, and half as many gardenias as lilacs. If she sold 10 lilacs, what is the total number of flowers sold on Tuesday?"""
    lilacs_sold = 10
    roses_sold = 3 * lilacs_sold
    gardenias_sold = lilacs_sold / 2
    total_flowers_sold = lilacs_sold + roses_sold + gardenias_sold
    result = total_flowers_sold
    return result

print(solution())