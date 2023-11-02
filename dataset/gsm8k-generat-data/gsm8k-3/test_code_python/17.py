def solution():
    """In a truck, there are 26 pink hard hats, 15 green hard hats, and 24 yellow hard hats. If Carl takes away 4 pink hard hats, and John takes away 6 pink hard hats and twice as many green hard hats as the number of pink hard hats that he removed, then calculate the total number of hard hats that remained in the truck."""
    # Define the initial number of hard hats
    pink_hats = 26
    green_hats = 15
    yellow_hats = 24

    # Carl takes away 4 pink hard hats
    pink_hats -= 4

    # John takes away 6 pink hard hats and twice as many green hard hats as the number of pink hard hats that he removed
    removed_pink = 6
    removed_green = 2 * removed_pink
    pink_hats -= removed_pink
    green_hats -= removed_green

    # Calculate the total number of hard hats that remained in the truck
    total_hats = pink_hats + green_hats + yellow_hats

    # Return the result
    result = total_hats
    return result

print(solution())