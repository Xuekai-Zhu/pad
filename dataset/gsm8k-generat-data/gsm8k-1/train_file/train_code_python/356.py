def solution():
    """Catriona has 8 goldfish in her aquarium. She has 4 more angelfish than goldfish. Also, she has twice as many guppies as angelfish. How many fish does Catriona have in her aquarium?"""
    goldfish = 8
    angelfish = goldfish + 4
    guppies = angelfish * 2
    total_fish = goldfish + angelfish + guppies
    result = total_fish
    return result

print(solution())