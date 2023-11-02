def solution():
    price_per_slice = 3.0
    slices_per_pie = 10
    num_pies = 6

    # Calculate the total number of slices of custard pie
    total_slices = num_pies * slices_per_pie

    # Calculate the total revenue earned by the pie shop
    total_revenue = total_slices * price_per_slice
    result = total_revenue
    return result

print(solution())