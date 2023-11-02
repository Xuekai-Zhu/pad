def solution():
    """James buys jars for his honey.  He has 5 hives that each produce 20 liters of honey.  Each jar can hold .5 liters.  How many jars will he need to buy if his friend is bringing his own jars for half the honey?"""
    # Define the amount of honey James needs to jar
    total_honey = 5 * 20 * 2  # 5 hives, 20 liters per hive, friend brings jars for half

    # Calculate the number of jars needed
    jars_needed = total_honey / 0.5

    # Display the number of jars needed
    result = jars_needed
    return result

print(solution())