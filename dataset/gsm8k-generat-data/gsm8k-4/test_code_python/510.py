def solution():
    """A pie shop charges $3 per slice of custard pie. They cut each whole pie into 10 slices. If they make 6 whole custard pies, how much money will the pie shop earn?"""
    # Define the price per slice and the number of slices per pie
    PRICE_PER_SLICE = 3
    SLICES_PER_PIE = 10

    # Calculate the total number of slices
    total_slices = 6 * SLICES_PER_PIE

    # Calculate the total earnings
    total_earnings = total_slices * PRICE_PER_SLICE

    # Return the result
    result = total_earnings
    return result

print(solution())