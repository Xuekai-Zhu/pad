def solution():
    """James buys jars for his honey. He has 5 hives that each produce 20 liters of honey. Each jar can hold .5 liters. How many jars will he need to buy if his friend is bringing his own jars for half the honey?"""
    num_hives = 5
    liters_per_hive = 20
    total_liters = num_hives * liters_per_hive
    jars_needed = (total_liters/2) / 0.5
    result = jars_needed
    return result

print(solution())