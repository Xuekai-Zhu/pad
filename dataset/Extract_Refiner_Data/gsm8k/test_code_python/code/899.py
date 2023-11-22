def solution():
    
    # Define the material for each type of mask
    SMALL_MASK_CAPACITY = 2
    LARGE_MASK_CAPACITY = 2.25

    # Define the number of each type of mask Jo wants to make
    small_masks = 20
    large_masks = 8

    # Calculate the total material needed for the small masks
    small_material_needed = small_masks * SMALL_MASK_CAPACITY

    # Calculate the total material needed for the large masks
    large_material_needed = large_masks * LARGE_MASK_CAPACITY

    # Calculate the total material needed for both types of masks
    total_material_needed = small_material_needed + large_material_needed

    # Display the total material needed
    result = total_material_needed
    return result

print(solution())