def solution():
    agate_stones = 30  # Agate has 30 precious stones
    olivine_stones = agate_stones + 5  # Olivine has 5 more precious stones than Agate
    diamond_stones = olivine_stones + 11  # Diamond has 11 more precious stones than Olivine

    # Calculate the total number of precious stones they have together
    total_stones = agate_stones + olivine_stones + diamond_stones
    result = total_stones
    return result

print(solution())