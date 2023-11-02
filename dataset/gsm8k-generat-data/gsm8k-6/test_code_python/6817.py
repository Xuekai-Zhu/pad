def solution():
    # Calculate the total area of the quilt
    quilt_area = 16 * 20  # in square feet

    # Calculate the number of patches needed
    patches_needed = quilt_area / 4  

    # Calculate the total cost of the first 10 patches
    cost_of_first_10 = 10 * 10  

    # Calculate the cost of the remaining patches
    cost_of_remaining_patches = (patches_needed - 10) * 5  

    # Calculate the total cost of all patches
    total_cost = cost_of_first_10 + cost_of_remaining_patches
    result = total_cost
    return result

print(solution())