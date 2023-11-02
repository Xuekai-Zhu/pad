def solution():
    """Collin has 25 flowers. Ingrid gives Collin a third of her 33 flowers. If each flower has 4 petals, how many petals does Collin have in total?"""
    collin_flowers = 25
    ingrid_flowers = 33
    ingrid_gives = ingrid_flowers / 3
    total_flowers = collin_flowers + ingrid_gives
    total_petals = total_flowers * 4
    result = total_petals
    return result

print(solution())