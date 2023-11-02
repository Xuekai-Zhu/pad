def solution():
    """Annie plants 3 pots of basil, 9 pots of rosemary, and 6 pots of thyme. Each basil plant has 4 leaves, each rosemary plant has 18 leaves, and each thyme plant has 30 leaves. How many leaves are there total?"""
    basil_pots = 3
    rosemary_pots = 9
    thyme_pots = 6
    basil_leaves_per_plant = 4
    rosemary_leaves_per_plant = 18
    thyme_leaves_per_plant = 30
    total_basil_leaves = basil_pots * basil_leaves_per_plant
    total_rosemary_leaves = rosemary_pots * rosemary_leaves_per_plant
    total_thyme_leaves = thyme_pots * thyme_leaves_per_plant
    total_leaves = total_basil_leaves + total_rosemary_leaves + total_thyme_leaves
    result = total_leaves
    return result

print(solution())