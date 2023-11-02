def solution():
    # Define price per slice and number of slices per pie
    price_per_slice = 7
    slices_per_pie = 6

    # Calculate total number of slices sold
    total_slices = 7 * slices_per_pie

    # Calculate total revenue from cheesecake sales
    total_revenue = total_slices * price_per_slice
    result = total_revenue
    return result

print(solution())