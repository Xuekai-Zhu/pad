def solution():
    
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