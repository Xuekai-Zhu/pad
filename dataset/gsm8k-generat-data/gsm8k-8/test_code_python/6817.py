def solution():
    # Calculate the total area of the quilt
    quilt_area = 16 * 20

    # Calculate the number of patches needed
    num_patches = quilt_area / 4

    # Calculate the cost of the first 10 patches
    first_10_patches_cost = 10 * 10

    # Calculate the cost of the remaining patches
    remaining_patches_cost = (num_patches - 10) * 5

    # Calculate the total cost of the patches
    total_cost = first_10_patches_cost + remaining_patches_cost
    result = total_cost
    return result

print(solution())