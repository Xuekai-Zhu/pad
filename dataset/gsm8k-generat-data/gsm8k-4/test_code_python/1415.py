def solution():
    """At Penny’s bakery, her famous blueberry cheesecakes are $7 a slice. Each cheesecake pie is cut into 6 thick slices. If she sells 7 cheesecake pies, how much money does she make?"""
    # Define the price per slice and the number of slices per pie
    PRICE_PER_SLICE = 7
    SLICES_PER_PIE = 6

    # Define the number of cheesecake pies sold
    cheesecake_pies_sold = 7

    # Calculate the total number of slices sold
    slices_sold = cheesecake_pies_sold * SLICES_PER_PIE

    # Calculate the total money made
    total_money = slices_sold * PRICE_PER_SLICE

    # return the result
    result = total_money
    return result

print(solution())