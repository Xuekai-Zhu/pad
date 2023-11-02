def solution():
    """James wants to build a 16-foot by 20-foot quilt.  He uses patches that are each 4 square feet.  The first 10 patches cost $10 each and then each patch after that cost half as much.  How much do the patches for the quilt cost?"""
    # Define the dimensions of the quilt and the size of each patch
    quilt_length = 16
    quilt_width = 20
    patch_size = 4

    # Calculate the total number of patches needed
    total_patches = (quilt_length * quilt_width) / patch_size

    # Calculate the cost of the first 10 patches
    first_10_cost = 10 * 10

    # Calculate the cost of the remaining patches
    remaining_patches = total_patches - 10
    remaining_cost = remaining_patches * 5

    # Calculate the total cost of all the patches
    total_cost = first_10_cost + remaining_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())