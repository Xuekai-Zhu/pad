def solution():
    """Rebecca bought 2 pies for the holiday weekend. Each pie was sliced into 8 slices. Rebecca ate 1 slice of each pie. Her family and friends ate 50% of the remaining pies over the weekend. On Sunday evening Rebecca and her husband each had another slice of pie. How many slices are remaining?"""
    # Define the number of slices per pie
    SLICES_PER_PIE = 8

    # Calculate the total number of slices before anyone ate a slice
    total_slices = 2 * SLICES_PER_PIE

    # Subtract the slices Rebecca ate
    total_slices -= 2

    # Calculate the number of slices eaten by Rebecca's family and friends
    remaining_slices = total_slices * 0.5

    # Subtract the slices eaten on Sunday evening
    remaining_slices -= 2

    # Display the remaining number of slices
    result = remaining_slices
    return result

print(solution())