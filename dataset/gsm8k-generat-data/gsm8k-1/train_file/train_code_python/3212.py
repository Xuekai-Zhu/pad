def solution():
    """In her bakery, Teal sells pumpkin pie and custard pie by the slice. The pumpkin pie is cut into 8 pieces. The custard pie is cut into 6 pieces. Pumpkin pie is $5 a slice. Custard pie is $6 a slice. If Teal sells 4 pumpkin pies and 5 custard pies, how much money does she make from her sales?"""
    pumpkin_pie_slices = 8
    pumpkin_pie_price = 5
    custard_pie_slices = 6
    custard_pie_price = 6
    pumpkin_pie_sales = 4 * pumpkin_pie_slices * pumpkin_pie_price
    custard_pie_sales = 5 * custard_pie_slices * custard_pie_price
    total_sales = pumpkin_pie_sales + custard_pie_sales
    result = total_sales
    return result

print(solution())