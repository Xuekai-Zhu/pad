def solution():
    """In her bakery, Teal sells pumpkin pie and custard pie by the slice.  The pumpkin pie is cut into 8 pieces.  The custard pie is cut into 6 pieces.  Pumpkin pie is $5 a slice.  Custard pie is $6 a slice.  If Teal sells 4 pumpkin pies and 5 custard pies, how much money does she make from her sales?"""
    # Define the cost per slice of each type of pie
    PUMPKIN_PRICE = 5
    CUSTARD_PRICE = 6

    # Define the number of slices in each pie
    PUMPKIN_SLICES = 8
    CUSTARD_SLICES = 6

    # Define the number of pies sold
    pumpkin_pies = 4
    custard_pies = 5

    # Calculate the total amount earned from pumpkin pie sales
    pumpkin_slices = pumpkin_pies * PUMPKIN_SLICES
    pumpkin_revenue = pumpkin_slices * PUMPKIN_PRICE

    # Calculate the total amount earned from custard pie sales
    custard_slices = custard_pies * CUSTARD_SLICES
    custard_revenue = custard_slices * CUSTARD_PRICE

    # Calculate the total revenue
    total_revenue = pumpkin_revenue + custard_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())