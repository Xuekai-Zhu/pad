def solution():
    """In her bakery, Teal sells pumpkin pie and custard pie by the slice. The pumpkin pie is cut into 8 pieces. The custard pie is cut into 6 pieces. Pumpkin pie is $5 a slice. Custard pie is $6 a slice. If Teal sells 4 pumpkin pies and 5 custard pies, how much money does she make from her sales?"""
    # Define the prices and number of slices per pie type
    pumpkin_price = 5
    custard_price = 6
    pumpkin_slices = 8
    custard_slices = 6

    # Calculate the total money earned from selling pumpkin pie
    pumpkin_slices_sold = 4 * pumpkin_slices
    pumpkin_money_earned = pumpkin_slices_sold * pumpkin_price

    # Calculate the total money earned from selling custard pie
    custard_slices_sold = 5 * custard_slices
    custard_money_earned = custard_slices_sold * custard_price

    # Calculate the total money earned from all sales
    total_money_earned = pumpkin_money_earned + custard_money_earned

    # return the result
    result = total_money_earned
    return result

print(solution())