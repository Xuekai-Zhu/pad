def solution():
    """Miggy's mom brought home 3 bags of birthday hats. Each bag has 15 hats. Miggy accidentally tore off 5 hats. During the party, only 25 hats were used. How many hats were unused?"""
    # Define the number of hats per bag and the total number of bags
    HATS_PER_BAG = 15
    TOTAL_BAGS = 3

    # Calculate the total number of hats before any were torn off
    total_hats = HATS_PER_BAG * TOTAL_BAGS

    # Subtract the torn hats and used hats from the total to get the unused hats
    unused_hats = total_hats - 5 - 25

    # return the result
    result = unused_hats
    return result

print(solution())