def solution():
    # Calculate the number of watermelon seeds Gwi has
    seeds_Gwi = 300 + 40  # Gwi has 40 more watermelon seeds than Bom
    # Calculate the number of watermelon seeds Yeon has
    seeds_Yeon = 3 * seeds_Gwi  # Yeon has three times as many seeds as Gwi
    # Calculate the total number of watermelon seeds they have together
    total_seeds = seeds_Gwi + seeds_Yeon + 300  # Bom has 300 seeds
    result = total_seeds
    return result

print(solution())