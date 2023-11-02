def solution():
    """Eliza has 4 siblings. The total height of all 5 siblings combined is 330 inches. Two of her siblings are both 66 inches tall. Another sibling is 60 inches tall. If Eliza is 2 inches shorter than the last sibling, how tall is Eliza?"""
    # Define the heights of the known siblings
    sibling1_height = 66
    sibling2_height = 66
    sibling3_height = 60

    # Calculate the total height of the known siblings
    known_siblings_height = sibling1_height + sibling2_height + sibling3_height

    # Calculate the height of the remaining two siblings combined
    remaining_siblings_height = 330 - known_siblings_height

    # Calculate the average height of the remaining two siblings
    avg_remaining_siblings_height = remaining_siblings_height / 2

    # Calculate Eliza's height
    eliza_height = avg_remaining_siblings_height - 2

    # Display Eliza's height
    result = eliza_height
    return result

print(solution())