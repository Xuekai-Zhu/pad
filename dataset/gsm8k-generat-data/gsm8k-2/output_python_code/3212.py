def solution():
    """In her bakery, Teal sells pumpkin pie and custard pie by the slice. The pumpkin pie is cut into 8 pieces. The custard pie is cut into 6 pieces. Pumpkin pie is $5 a slice. Custard pie is $6 a slice. If Teal sells 4 pumpkin pies and 5 custard pies, how much money does she make from her sales?"""
    pumpkin_slices_per_pie = 8
    custard_slices_per_pie = 6
    pumpkin_price_per_slice = 5
    custard_price_per_slice = 6
    pumpkin_pies_sold = 4
    custard_pies_sold = 5
    total_pumpkin_slices = pumpkin_pies_sold * pumpkin_slices_per_pie
    total_custard_slices = custard_pies_sold * custard_slices_per_pie
    total_sales = (total_pumpkin_slices * pumpkin_price_per_slice) + (total_custard_slices * custard_price_per_slice)
    result = total_sales
    return result

print(solution())