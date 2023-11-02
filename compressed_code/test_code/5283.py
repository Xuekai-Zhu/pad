def solution():
    
    pie_slices_per_pie = 4
    price_per_slice = 5
    pies_sold = 9
    total_slices_sold = pie_slices_per_pie * pies_sold
    total_money_made = total_slices_sold * price_per_slice
    result = total_money_made
    return result

print(solution())