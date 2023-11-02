def solution():
    """Mandy bought 3 packs of black shirts and 3 packs of yellow shirts for her tennis team. The black shirts come in packs of 5, and the yellow shirts come in packs of 2. How many shirts did Mandy buy in all?"""
    # Define the number of packs and shirts per pack for each color
    BLACK_PACKS = 3
    BLACK_SHIRTS_PER_PACK = 5
    YELLOW_PACKS = 3
    YELLOW_SHIRTS_PER_PACK = 2

    # Calculate the total number of black shirts bought
    total_black_shirts = BLACK_PACKS * BLACK_SHIRTS_PER_PACK

    # Calculate the total number of yellow shirts bought
    total_yellow_shirts = YELLOW_PACKS * YELLOW_SHIRTS_PER_PACK

    # Calculate the total number of shirts bought
    total_shirts = total_black_shirts + total_yellow_shirts

    # Display the total number of shirts bought
    result = total_shirts
    return result

print(solution())