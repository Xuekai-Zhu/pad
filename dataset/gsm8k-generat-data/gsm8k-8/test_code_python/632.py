def solution():
    # Define the number of watermelon seeds Bom has
    bom_seeds = 300

    # Calculate the number of seeds Gwi has
    gwi_seeds = bom_seeds + 40

    # Calculate the number of seeds Yeon has
    yeon_seeds = 3 * gwi_seeds

    # Calculate the total number of seeds
    total_seeds = bom_seeds + gwi_seeds + yeon_seeds

    result = total_seeds
    return result

print(solution())