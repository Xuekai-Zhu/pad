def solution():
    """A pie shop charges $5 for a slice of pie. They cut each whole pie into 4 slices. How much money will the pie shop make if they sell 9 pies?"""
    slice_price = 5
    slices_per_pie = 4
    pies_sold = 9
    total_slices = pies_sold * slices_per_pie
    total_money = total_slices * slice_price
    result = total_money
    return result

print(solution())