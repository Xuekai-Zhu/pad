def solution():
    quilt_length = 16
    quilt_width = 20
    patch_size = 4
    num_patches = (quilt_length * quilt_width) / patch_size

    # Calculate the cost of the first 10 patches
    first_10_patches_cost = 10 * 10  # $10 each

    # Calculate the cost of each patch after the first 10
    cost_per_patch = 5  # Half the cost of the first 10 patches

    # Calculate the total cost of all patches
    total_cost = first_10_patches_cost + ((num_patches - 10) * cost_per_patch)
    result = total_cost
    return result

print(solution())