def solution():
    num_hives = 2
    bees_in_hive1 = 1000
    honey_in_hive1 = 500

    # Calculate the number of bees in hive2, which is 20% less than hive1
    bees_in_hive2 = bees_in_hive1 - (0.20 * bees_in_hive1)

    # Calculate the increase in production of honey per bee in hive2, which is 40%
    honey_per_bee_increase = 0.40

    # Calculate the total number of bees in both hives
    total_bees = bees_in_hive1 + bees_in_hive2

    # Calculate the total amount of honey produced by both hives
    total_honey = honey_in_hive1 + (bees_in_hive2 * honey_per_bee_increase * honey_in_hive1)

    result = total_honey
    return result

print(solution())