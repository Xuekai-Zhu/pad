def solution():
    bom_seeds = 300  # Bom has 300 watermelon seeds
    gwi_seeds = bom_seeds + 40  # Gwi has 40 more seeds than Bom
    yeon_seeds = 3 * gwi_seeds  # Yeon has three times as many seeds as Gwi
    
    # Calculate the total number of seeds
    total_seeds = bom_seeds + gwi_seeds + yeon_seeds
    result = total_seeds
    return result

print(solution())