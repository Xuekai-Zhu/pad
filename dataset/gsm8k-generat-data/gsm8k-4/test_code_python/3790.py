def solution():
    """James buys jars for his honey. He has 5 hives that each produce 20 liters of honey. Each jar can hold .5 liters. How many jars will he need to buy if his friend is bringing his own jars for half the honey?"""
    # Define the number of hives and liters of honey produced by each hive
    num_hives = 5
    liters_per_hive = 20

    # Calculate the total liters of honey produced
    total_liters = num_hives * liters_per_hive

    # Calculate the total number of jars needed for all the honey
    total_jars = total_liters / 0.5

    # Calculate the number of jars needed for half the honey (which will be brought by a friend)
    friend_jars = total_jars / 2

    # Calculate the total number of jars needed to be bought by James
    james_jars = total_jars - friend_jars

    result = james_jars
    return result

print(solution())