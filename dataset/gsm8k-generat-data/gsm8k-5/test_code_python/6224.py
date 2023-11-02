def solution():
    # Calculate the total height of Eliza's siblings and subtract the heights of the known siblings
    remaining_height = 330 - (66 * 2) - 60

    # Divide the remaining height by the number of remaining siblings (including Eliza)
    eliza_height = remaining_height / 2 - 2

    result = eliza_height
    return result

print(solution())