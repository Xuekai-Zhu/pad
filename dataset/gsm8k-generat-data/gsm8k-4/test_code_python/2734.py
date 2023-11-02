def solution():
    """Annie plants 3 pots of basil, 9 pots of rosemary, and 6 pots of thyme. Each basil plant has 4 leaves, each rosemary plant has 18 leaves, and each thyme plant has 30 leaves. How many leaves are there total?"""
    # Calculate the total number of leaves for basil plants
    basil_leaves = 3 * 4

    # Calculate the total number of leaves for rosemary plants
    rosemary_leaves = 9 * 18

    # Calculate the total number of leaves for thyme plants
    thyme_leaves = 6 * 30

    # Calculate the total number of leaves
    total_leaves = basil_leaves + rosemary_leaves + thyme_leaves

    # return the result
    result = total_leaves
    return result

print(solution())