def solution():
    total_area = 16 * 20  # Total area of the quilt in square feet
    patch_area = 4  # Area of each patch in square feet
    num_patches = total_area / patch_area  # Number of patches needed

    # Calculate the cost of the first 10 patches
    first_10_patches_cost = 10 * 10

    # Calculate the cost of the remaining patches
    remaining_patches = num_patches - 10
    remaining_patches_cost = remaining_patches * 5

    # Calculate the total cost of the patches
    total_cost = first_10_patches_cost + remaining_patches_cost
    result = total_cost
    return result

print(solution())