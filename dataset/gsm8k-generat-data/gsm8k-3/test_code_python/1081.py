def solution():
    """John has 2 hives of bees. One of the hives has 1000 bees and produces 500 liters of honey. The second has 20% fewer bees but each bee produces 40% more honey. How much honey does he produce?"""
    # Calculate the honey produced by the first hive
    hive1_honey = 500

    # Calculate the number of bees in the second hive
    hive2_bees = 0.8 * 1000

    # Calculate the honey produced by each bee in the second hive
    hive2_honey_per_bee = 1.4

    # Calculate the total honey produced by the second hive
    hive2_honey = hive2_bees * hive2_honey_per_bee

    # Calculate the total honey produced by both hives
    total_honey = hive1_honey + hive2_honey

    # Display the total honey produced
    result = total_honey
    return result

print(solution())