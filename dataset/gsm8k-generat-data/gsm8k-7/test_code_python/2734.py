def solution():
    num_basil_pots = 3
    basil_leaves_per_pot = 4

    num_rosemary_pots = 9
    rosemary_leaves_per_pot = 18

    num_thyme_pots = 6
    thyme_leaves_per_pot = 30

    # Calculate the total number of basil leaves
    total_basil_leaves = num_basil_pots * basil_leaves_per_pot

    # Calculate the total number of rosemary leaves
    total_rosemary_leaves = num_rosemary_pots * rosemary_leaves_per_pot

    # Calculate the total number of thyme leaves
    total_thyme_leaves = num_thyme_pots * thyme_leaves_per_pot

    # Calculate the total number of leaves
    total_leaves = total_basil_leaves + total_rosemary_leaves + total_thyme_leaves
    result = total_leaves
    return result

print(solution())