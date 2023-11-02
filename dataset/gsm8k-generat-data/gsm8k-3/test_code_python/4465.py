def solution():
    """June found 2 birds nest with 5 eggs each in 1 tree and 1 nest with 3 eggs in another tree.  There was also a nest with 4 eggs in her front yard.  How many birds eggs did she find?"""
    # Define the number of eggs in each nest
    NEST1_EGGS = 5
    NEST2_EGGS = 5
    NEST3_EGGS = 3
    NEST4_EGGS = 4

    # Calculate the total number of eggs found
    total_eggs = (2 * NEST1_EGGS) + NEST3_EGGS + NEST4_EGGS

    # Display the total number of eggs found
    result = total_eggs
    return result

print(solution())