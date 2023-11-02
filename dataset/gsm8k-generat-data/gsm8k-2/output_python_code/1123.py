def solution():
    """When all her clothes are washed and in her closet, Brie has 12 blouses, 6 skirts, and 8 slacks. Today in her hamper, she has 75% of her blouses, 50% of her skirts, and 25% of her slacks. How many pieces of clothing will she need to put in the washer?"""
    total_blouses = 12
    total_skirts = 6
    total_slacks = 8
    hamper_blouses = total_blouses * 0.75
    hamper_skirts = total_skirts * 0.5
    hamper_slacks = total_slacks * 0.25
    total_hamper = hamper_blouses + hamper_skirts + hamper_slacks
    result = total_hamper
    return result

print(solution())