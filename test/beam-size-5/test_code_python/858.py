def solution():
    
    # Define the number of banana bread loaves and slices per loaf
    NUM_LOAVES = 2
    SLICES_PER_LOAF = 8

    # Calculate the total number of slices
    total_slices = NUM_LOAVES * SLICES_PER_LOAF

    # Calculate the number of fundraiser sold
    fundraiser_slices = total_slices * 0.5

    # Calculate the total amount raised
    total_raised = fundraiser_slices * 0.5

    # Display the total amount raised
    result = total_raised
    return result

print(solution())