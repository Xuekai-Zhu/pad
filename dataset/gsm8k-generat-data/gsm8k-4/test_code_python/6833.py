def solution():
    """A pie shop charges $5 for a slice of pie. They cut each whole pie into 4 slices. How much money will the pie shop make if they sell 9 pies?"""
    # Define the price per slice and the number of slices per pie
    PRICE_PER_SLICE = 5
    SLICES_PER_PIE = 4

    # Define the number of pies sold
    pies_sold = 9

    # Calculate the total number of slices sold
    total_slices = pies_sold * SLICES_PER_PIE

    # Calculate the total revenue generated
    total_revenue = total_slices * PRICE_PER_SLICE

    # return the result
    result = total_revenue
    return result

print(solution())