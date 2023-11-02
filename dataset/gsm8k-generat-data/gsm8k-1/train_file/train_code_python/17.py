def solution():
    """In a truck, there are 26 pink hard hats, 15 green hard hats, and 24 yellow hard hats. If Carl takes away 4 pink hard hats, and John takes away 6 pink hard hats
    and twice as many green hard hats as the number of pink hard hats that he removed, then calculate the total number of hard hats that remained in the truck."""
    pink_hats = 26
    green_hats = 15
    yellow_hats = 24

    # Carl takes away 4 pink hard hats
    pink_hats = pink_hats - 4

    # John takes away 6 pink hard hats and twice as many green hard hats as the number of pink hard hats that he removed
    pink_removed = 6
    green_removed = pink_removed * 2
    pink_hats = pink_hats - pink_removed
    green_hats = green_hats - green_removed

    # Total number of hard hats that remained in the truck
    total_hats = pink_hats + green_hats + yellow_hats
    result = total_hats

    return result

print(solution())