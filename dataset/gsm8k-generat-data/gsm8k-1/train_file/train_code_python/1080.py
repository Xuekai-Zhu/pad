def solution():
    """John has 2 hives of bees. One of the hives has 1000 bees and produces 500 liters of honey. The second has 20% fewer bees but each bee produces 40% more honey. How much honey does he produce?"""
    hive1_bees = 1000
    hive1_honey = 500
    hive2_bees = hive1_bees * 0.8
    hive2_honey_per_bee = 1.4
    hive2_honey = hive2_bees * hive2_honey_per_bee * hive1_honey
    total_honey = hive1_honey + hive2_honey
    result = total_honey
    return result

print(solution())