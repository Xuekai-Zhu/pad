def solution():
    """James buys jars for his honey. He has 5 hives that each produce 20 liters of honey. Each jar can hold .5 liters. How many jars will he need to buy if his friend is bringing his own jars for half the honey?"""
    total_honey = 5 * 20
    jars_needed = total_honey / 0.5
    jars_needed = round(jars_needed / 2)
    result = jars_needed
    return result

print(solution())