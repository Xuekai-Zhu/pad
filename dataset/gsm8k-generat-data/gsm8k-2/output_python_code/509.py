def solution():
    """A pie shop charges $3 per slice of custard pie. They cut each whole pie into 10 slices. If they make 6 whole custard pies, how much money will the pie shop earn?"""
    slices_per_pie = 10
    price_per_slice = 3
    pies = 6
    total_slices = slices_per_pie * pies
    total_earnings = total_slices * price_per_slice
    result = total_earnings
    return result

print(solution())