def solution():
    # Calculate the number of gold coins per chest
    gold_per_chest = 3500 // 5

    # Calculate the total number of silver coins
    total_silver = 500

    # Calculate the number of bronze coins
    bronze = 2 * total_silver

    # Calculate the total number of coins per chest
    total_per_chest = gold_per_chest + (total_silver + bronze) // 5
    
    result = total_per_chest
    return result

print(solution())