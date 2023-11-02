def solution():
    pumpkin_pie_price = 5
    custard_pie_price = 6
    pumpkin_pie_slices = 8
    custard_pie_slices = 6
    total_pumpkin_pie_slices_sold = 4 * pumpkin_pie_slices
    total_custard_pie_slices_sold = 5 * custard_pie_slices
    total_slices_sold = total_pumpkin_pie_slices_sold + total_custard_pie_slices_sold
    total_price = (total_pumpkin_pie_slices_sold * pumpkin_pie_price) + (total_custard_pie_slices_sold * custard_pie_price)
    result = total_price
    
    return result

print(solution())