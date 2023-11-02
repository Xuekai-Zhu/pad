def solution():
    """Catriona has 8 goldfish in her aquarium. She has 4 more angelfish than goldfish. Also, she has twice as many guppies as angelfish. How many fish does Catriona have in her aquarium?"""
    # Define the number of goldfish and calculate the number of angelfish
    goldfish = 8
    angelfish = goldfish + 4

    # Calculate the number of guppies
    guppies = angelfish * 2

    # Calculate the total number of fish
    total_fish = goldfish + angelfish + guppies

    # Display the total number of fish
    result = total_fish
    return result

print(solution())