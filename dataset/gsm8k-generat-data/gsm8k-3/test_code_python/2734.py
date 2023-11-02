def solution():
    """Annie plants 3 pots of basil, 9 pots of rosemary, and 6 pots of thyme. Each basil plant has 4 leaves, each rosemary plant has 18 leaves, and each thyme plant has 30 leaves. How many leaves are there total?"""
    # Define the number of pots and leaves for each type of plant
    BASIL_POTS = 3
    ROSEMARY_POTS = 9
    THYME_POTS = 6
    BASIL_LEAVES = 4
    ROSEMARY_LEAVES = 18
    THYME_LEAVES = 30

    # Calculate the total number of leaves for each type of plant
    basil_total_leaves = BASIL_POTS * BASIL_LEAVES
    rosemary_total_leaves = ROSEMARY_POTS * ROSEMARY_LEAVES
    thyme_total_leaves = THYME_POTS * THYME_LEAVES

    # Calculate the total number of leaves for all plants
    total_leaves = basil_total_leaves + rosemary_total_leaves + thyme_total_leaves

    # Display the total number of leaves
    result = total_leaves
    return result

print(solution())