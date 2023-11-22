def solution():
    
    # Define the number of banana bread loaves Paige can bake in one hour
    LOAVES_PER_HOUR = 2

    # Define the number of slices per banana bread loaf
    SLICES_PER_LOAF = 8

    # Define the amount raised per slice
    SLICE_PRICE = 0.5

    # Calculate the total number of slices Paige baked
    total_slices = LOAVES_PER_HOUR * SLICES_PER_LOAF

    # Calculate the total amount raised
    total_raised = total_slices * SLICE_PRICE

    # Display the total amount raised
    result = total_raised
    return result

print(solution())