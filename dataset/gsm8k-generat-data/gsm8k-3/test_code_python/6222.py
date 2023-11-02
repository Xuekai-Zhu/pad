def solution():
    """Jina likes to collect mascots. She has 5 teddies, 3 times more bunnies, and a koala bear. Her mom decided to give her two additional teddies for every bunny she has. How many mascots Jina has in total?"""
    # Define the number of teddies and bunnies
    teddies = 5
    bunnies = 3 * teddies

    # Calculate the number of bonus teddies
    bonus_teddies = 2 * bunnies

    # Calculate the total number of mascots
    total_mascots = teddies + bunnies + bonus_teddies + 1  # add 1 for the koala bear

    # Display the total number of mascots
    result = total_mascots
    return result

print(solution())