def solution():
    hive1_bees = 1000
    hive1_honey_per_bee = 500 / hive1_bees

    hive2_bees = hive1_bees * 0.8
    hive2_honey_per_bee = hive1_honey_per_bee * 1.4

    hive2_honey = hive2_bees * hive2_honey_per_bee
    total_honey = 500 + hive2_honey
    result = total_honey
    return result

print(solution())