def solution():
    """
    John has 2 hives of bees. One of the hives has 1000 bees and produces 500 liters of honey. 
    The second has 20% fewer bees but each bee produces 40% more honey. How much honey does he produce?
    """
    # Define the initial number of bees and amount of honey for the first hive
    bees_1 = 1000
    honey_1 = 500

    # Calculate the number of bees and amount of honey for the second hive
    bees_2 = int(bees_1 * 0.8)
    honey_per_bee = honey_1 / bees_1
    honey_2 = bees_2 * honey_per_bee * 1.4

    # Calculate the total amount of honey produced by both hives
    total_honey = honey_1 + honey_2

    # Return the result
    result = total_honey
    return result

print(solution())