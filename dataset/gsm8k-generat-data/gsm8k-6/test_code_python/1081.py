def solution():
    # Calculate the number of bees and honey produced by the second hive
    bees_second_hive = 0.8 * 1000  # 20% fewer bees than the first hive
    honey_per_bee_second_hive = 1.4  # 40% more honey per bee than the first hive
    honey_second_hive = bees_second_hive * honey_per_bee_second_hive  # total honey produced by the second hive

    # Calculate the total honey produced by both hives
    total_honey = 500 + honey_second_hive

    result = total_honey
    return result

print(solution())