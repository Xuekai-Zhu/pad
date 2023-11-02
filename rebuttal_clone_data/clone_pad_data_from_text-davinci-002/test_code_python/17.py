def solution():
    """In a truck, there are 26 pink hard hats, 15 green hard hats, and 24 yellow hard hats. If Carl takes away 4 pink hard hats, and John takes away 6 pink hard hats and twice as many green hard hats as the number of pink hard hats that he removed, then calculate the total number of hard hats that remained in the truck."""
    pink_hard_hats = 26
    green_hard_hats = 15
    yellow_hard_hats = 24
    total_hard_hats = pink_hard_hats + green_hard_hats + yellow_hard_hats
    pink_hard_hats_removed = 4 + 6
    green_hard_hats_removed = 2 * pink_hard_hats_removed
    total_hard_hats_removed = pink_hard_hats_removed + green_hard_hats_removed
    result = total_hard_hats - total_hard_hats_removed
    return result

print(solution())