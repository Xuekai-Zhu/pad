def solution():
    # Calculate the honey produced by the first hive
    bees_first_hive = 1000
    honey_per_bee_first_hive = 500 / bees_first_hive
    total_honey_first_hive = bees_first_hive * honey_per_bee_first_hive

    # Calculate the honey produced by the second hive
    bees_second_hive = bees_first_hive * 0.8
    honey_per_bee_second_hive = honey_per_bee_first_hive * 1.4
    total_honey_second_hive = bees_second_hive * honey_per_bee_second_hive

    # Calculate the total honey produced by both hives
    total_honey = total_honey_first_hive + total_honey_second_hive
    result = total_honey
    return result

print(solution())