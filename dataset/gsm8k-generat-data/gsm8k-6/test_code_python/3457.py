def solution():
    # Calculate the number of gold coins in each chest
    gold_per_chest = 3500 // 5  # integer division to get equal distribution

    # Calculate the total number of silver coins and distribute equally across the chests
    total_silver = 500
    silver_per_chest = total_silver // 5

    # Calculate the total number of bronze coins and distribute equally across the chests
    total_bronze = total_silver * 2
    bronze_per_chest = total_bronze // 5

    # Calculate the total number of coins in each chest
    total_per_chest = gold_per_chest + silver_per_chest + bronze_per_chest

    result = total_per_chest
    return result

print(solution())