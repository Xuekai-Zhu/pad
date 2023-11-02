def solution():
    """Catriona has 8 goldfish in her aquarium. She has 4 more angelfish than goldfish. Also, she has twice as many guppies as angelfish. How many fish does Catriona have in her aquarium?"""
    # Define the initial number of goldfish
    goldfish = 8

    # Calculate the number of angelfish
    angelfish = goldfish + 4

    # Calculate the number of guppies
    guppies = 2 * angelfish

    # Calculate the total number of fish in the aquarium
    total_fish = goldfish + angelfish + guppies

    # return the result
    result = total_fish
    return result

print(solution())