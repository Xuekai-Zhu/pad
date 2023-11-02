def solution():
    """A pie shop charges $5 for a slice of pie. They cut each whole pie into 4 slices. How much money will the pie shop make if they sell 9 pies?"""
    pie_slices_per_pie = 4
    price_per_slice = 5
    pies_sold = 9
    total_slices_sold = pie_slices_per_pie * pies_sold
    total_money_made = total_slices_sold * price_per_slice
    result = total_money_made
    return result

print(solution())