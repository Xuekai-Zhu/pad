def solution():
    """Mandy bought 3 packs of black shirts and 3 packs of yellow shirts for her tennis team. The black shirts come in packs of 5, and the yellow shirts come in packs of 2. How many shirts did Mandy buy in all?"""
    # Define the number of packs of black and yellow shirts
    black_packs = 3
    yellow_packs = 3

    # Calculate the total number of black shirts
    black_shirts = black_packs * 5

    # Calculate the total number of yellow shirts
    yellow_shirts = yellow_packs * 2

    # Calculate the total number of shirts
    total_shirts = black_shirts + yellow_shirts

    # Return the result
    result = total_shirts
    return result

print(solution())