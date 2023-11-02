def solution():
    """When all her clothes are washed and in her closet, Brie has 12 blouses, 6 skirts, and 8 slacks.  Today in her hamper, she has 75% of her blouses, 50% of her skirts, and 25% of her slacks.  How many pieces of clothing will she need to put in the washer?"""
    # Calculate the number of blouses in the hamper
    blouses_hamper = 0.75 * 12

    # Calculate the number of skirts in the hamper
    skirts_hamper = 0.5 * 6

    # Calculate the number of slacks in the hamper
    slacks_hamper = 0.25 * 8

    # Calculate the total number of clothing items in the hamper
    total_hamper = blouses_hamper + skirts_hamper + slacks_hamper

    # Calculate the number of clothing items that need to be washed
    to_wash = total_hamper - (12 + 6 + 8)

    # Display the number of clothing items to be washed
    result = to_wash
    return result

print(solution())