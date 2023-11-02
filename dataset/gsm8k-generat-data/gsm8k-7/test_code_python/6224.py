def solution():
    num_siblings = 5
    total_height = 330
    sibling1_height = 66
    sibling2_height = 66
    sibling3_height = 60

    # Calculate the total height of the three known siblings
    known_siblings_height = sibling1_height + sibling2_height + sibling3_height

    # Calculate the height of the two unknown siblings combined
    unknown_siblings_height = total_height - known_siblings_height

    # Calculate the average height of the two unknown siblings
    avg_height = unknown_siblings_height / 2

    # Calculate Eliza's height (2 inches shorter than the last sibling)
    eliza_height = avg_height - 2
    result = eliza_height
    return result

print(solution())