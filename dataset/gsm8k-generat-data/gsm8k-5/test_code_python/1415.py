def solution():
    price_per_slice = 7  # Each slice of blueberry cheesecake costs $7
    slices_per_pie = 6  # Each cheesecake pie is cut into 6 slices
    pies_sold = 7  # Penny sells 7 cheesecake pies

    # Calculate the total number of slices sold
    total_slices = pies_sold * slices_per_pie

    # Calculate the total amount of money made
    total_money = total_slices * price_per_slice
    result = total_money
    return result

print(solution())