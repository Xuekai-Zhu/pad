def solution():
    """When all her clothes are washed and in her closet, Brie has 12 blouses, 6 skirts, and 8 slacks. Today in her hamper, she has 75% of her blouses, 50% of her skirts, and 25% of her slacks. How many pieces of clothing will she need to put in the washer?"""
    # Define the initial number of blouses, skirts, and slacks
    initial_blouses = 12
    initial_skirts = 6
    initial_slacks = 8

    # Calculate the number of blouses, skirts, and slacks in the hamper
    hamper_blouses = initial_blouses * 0.75
    hamper_skirts = initial_skirts * 0.5
    hamper_slacks = initial_slacks * 0.25

    # Calculate the total number of clothes in the hamper
    total_hamper = hamper_blouses + hamper_skirts + hamper_slacks

    # Round up the total to the nearest integer
    clothes_to_wash = int(total_hamper + 0.5)

    # Return the result
    result = clothes_to_wash
    return result

print(solution())