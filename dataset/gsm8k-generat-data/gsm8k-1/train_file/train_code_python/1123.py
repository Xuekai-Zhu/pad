def solution():
    """
    When all her clothes are washed and in her closet, Brie has 12 blouses, 6 skirts, and 8 slacks. Today in her hamper, she has 75% 
    of her blouses, 50% of her skirts, and 25% of her slacks. How many pieces of clothing will she need to put in the washer?
    """
    blouses_clean = 12 * (1 - 0.75)
    skirts_clean = 6 * (1 - 0.5)
    slacks_clean = 8 * (1 - 0.25)
    total_clean = blouses_clean + skirts_clean + slacks_clean
    result = total_clean
    return result

print(solution())