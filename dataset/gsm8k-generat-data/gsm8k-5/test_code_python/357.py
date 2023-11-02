def solution():
    goldfish = 8  # Catriona has 8 goldfish
    angelfish = goldfish + 4  # Catriona has 4 more angelfish than goldfish
    guppies = angelfish * 2  # Catriona has twice as many guppies as angelfish

    # Calculate the total number of fish in Catriona's aquarium
    total_fish = goldfish + angelfish + guppies
    result = total_fish
    return result

print(solution())