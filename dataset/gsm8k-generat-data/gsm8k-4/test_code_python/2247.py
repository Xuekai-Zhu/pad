def solution():
    """Billy is counting the rings in two trees. Weather fluctuations in this area mean that each tree's rings are in groups of two fat rings and four thin rings. If Billy counts 70 ring groups in the first tree and 40 ring groups in the second tree, how much older is the first tree? (Trees grow 1 ring per year.)"""
    # Define the number of fat and thin rings in each group
    FAT_RINGS = 2
    THIN_RINGS = 4

    # Calculate the total number of rings in each tree
    tree1_rings = (FAT_RINGS + THIN_RINGS) * 70
    tree2_rings = (FAT_RINGS + THIN_RINGS) * 40

    # Calculate the age difference between the trees
    age_difference = (tree1_rings - tree2_rings) / 2

    # return the result
    result = age_difference
    return result

print(solution())