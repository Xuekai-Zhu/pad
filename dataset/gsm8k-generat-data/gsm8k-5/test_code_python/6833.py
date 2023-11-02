def solution():
    price_per_slice = 5  # The pie shop charges $5 per slice of pie
    slices_per_pie = 4  # Each pie is cut into 4 equal slices
    pies_sold = 9  # The pie shop sells 9 pies

    # Calculate the total number of slices sold
    total_slices = pies_sold * slices_per_pie

    # Calculate the total amount of money made
    total_money = total_slices * price_per_slice
    result = total_money
    return result

print(solution())