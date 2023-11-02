def solution():
    """At Penny’s bakery, her famous blueberry cheesecakes are $7 a slice.  Each cheesecake pie is cut into 6 thick slices.  If she sells 7 cheesecake pies, how much money does she make?"""
    # Define the price per slice
    PRICE_PER_SLICE = 7

    # Define the number of slices per cheesecake pie
    SLICES_PER_PIE = 6

    # Define the number of cheesecake pies sold
    pies_sold = 7

    # Calculate the total number of slices sold
    total_slices_sold = pies_sold * SLICES_PER_PIE

    # Calculate the total amount of money made
    total_money_made = total_slices_sold * PRICE_PER_SLICE

    # Display the total money made
    result = total_money_made
    return result

print(solution())