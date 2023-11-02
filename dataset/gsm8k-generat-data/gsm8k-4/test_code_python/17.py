def solution():
    """In a truck, there are 26 pink hard hats, 15 green hard hats, and 24 yellow hard hats. If Carl takes away 4 pink hard hats, and John takes away 6 pink hard hats and twice as many green hard hats as the number of pink hard hats that he removed, then calculate the total number of hard hats that remained in the truck."""
    # Define the initial numbers of hard hats
    pink_hats = 26
    green_hats = 15
    yellow_hats = 24

    # Update the number of pink hats after Carl takes 4 of them
    pink_hats -= 4

    # Update the number of pink and green hats after John takes 6 pink hats and twice as many green hats
    pink_hats -= 6
    green_hats -= (2 * 6)

    # Calculate the total number of hard hats remaining
    total_hats = pink_hats + green_hats + yellow_hats

    # Return the result
    result = total_hats
    return result

print(solution())