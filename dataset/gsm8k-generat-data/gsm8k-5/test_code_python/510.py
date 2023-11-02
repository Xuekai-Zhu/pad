def solution():
    price_per_slice = 3  # The pie shop charges $3 per slice
    slices_per_pie = 10  # Each whole pie is cut into 10 slices
    pies = 6  # The pie shop makes 6 whole custard pies

    # Calculate the total number of slices
    total_slices = pies * slices_per_pie

    # Calculate the total earnings of the pie shop
    total_earnings = total_slices * price_per_slice
    result = total_earnings
    return result

print(solution())