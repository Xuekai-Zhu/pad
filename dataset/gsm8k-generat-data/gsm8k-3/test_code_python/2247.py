def solution():
    """Billy is counting the rings in two trees. Weather fluctuations in this area mean that each tree's rings are in groups of two fat rings and four thin rings. If Billy counts 70 ring groups in the first tree and 40 ring groups in the second tree, how much older is the first tree? (Trees grow 1 ring per year.)"""
    # Define the number of rings in each group
    FAT_RING = 2
    THIN_RING = 1

    # Define the number of rings in each cycle (2 fat rings and 4 thin rings)
    CYCLE_TOTAL = FAT_RING * 2 + THIN_RING * 4

    # Calculate the number of cycles in each tree
    tree1_cycles = 70 / 6
    tree2_cycles = 40 / 6

    # Calculate the age of each tree
    tree1_age = tree1_cycles * 2
    tree2_age = tree2_cycles * 2

    # Calculate the difference in age between the two trees
    age_difference = tree1_age - tree2_age

    # Display the age difference
    result = age_difference
    return result

print(solution())