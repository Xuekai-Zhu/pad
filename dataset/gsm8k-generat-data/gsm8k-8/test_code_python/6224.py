def solution():
    # Calculate the combined height of the three known siblings
    known_height = 66 + 66 + 60

    # Calculate the remaining height for all 5 siblings combined
    remaining_height = 330 - known_height

    # Calculate the average height of the 5 siblings, excluding Eliza
    average_height = remaining_height / 2

    # Calculate Eliza's height
    eliza_height = average_height - 2
    result = eliza_height
    return result

print(solution())