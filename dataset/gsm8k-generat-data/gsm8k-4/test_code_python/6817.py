def solution():
    """James wants to build a 16-foot by 20-foot quilt. He uses patches that are each 4 square feet. The first 10 patches cost $10 each and then each patch after that cost half as much. How much do the patches for the quilt cost?"""
    # Define the dimensions of the quilt and the size of each patch
    quilt_length = 16  # feet
    quilt_width = 20  # feet
    patch_size = 4  # square feet

    # Calculate the total area of the quilt in square feet
    quilt_area = quilt_length * quilt_width

    # Calculate the number of patches needed to cover the quilt
    total_patches = quilt_area / patch_size

    # Calculate the cost of the first 10 patches
    first_10_patches_cost = 10 * 10

    # Calculate the cost of the remaining patches
    remaining_patches = total_patches - 10
    remaining_patches_cost = remaining_patches * 5

    # Calculate the total cost of all the patches
    total_cost = first_10_patches_cost + remaining_patches_cost

    # return the result
    result = total_cost
    return result

print(solution())