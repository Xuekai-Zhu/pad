def solution():
    """Rebecca bought 2 pies for the holiday weekend. Each pie was sliced into 8 slices. Rebecca ate 1 slice of each pie. Her family and friends ate 50% of the remaining pies over the weekend. On Sunday evening Rebecca and her husband each had another slice of pie. How many slices are remaining?"""
    # Calculate the total number of slices
    total_slices = 2 * 8

    # Calculate the number of slices Rebecca ate
    rebecca_slices = 2

    # Calculate the number of remaining slices after Rebecca ate
    remaining_slices = total_slices - rebecca_slices

    # Calculate the number of slices eaten by family and friends
    guests_slices = remaining_slices * 0.5

    # Calculate the number of remaining slices after guests ate
    remaining_slices -= guests_slices

    # Calculate the number of slices Rebecca and her husband ate on Sunday evening
    remaining_slices -= 2

    # Return the result
    result = remaining_slices
    return result

print(solution())