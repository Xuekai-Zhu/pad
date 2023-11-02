def solution():
    price_per_slice = 5
    slices_per_pie = 4
    num_pies_sold = 9

    # Calculate the total number of slices sold
    total_slices_sold = num_pies_sold * slices_per_pie

    # Calculate the total revenue from pie sales
    total_revenue = total_slices_sold * price_per_slice
    result = total_revenue
    return result

print(solution())