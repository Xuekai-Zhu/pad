def solution():
    """Jack is trying to stack cans in his emergency bunker. If he can fit 12 cans in one row, 4 rows on one shelf, and 10 shelves in one closet, how many cans can he store in each closet?"""
    cans_per_row = 12
    rows_per_shelf = 4
    shelves_per_closet = 10
    cans_per_closet = cans_per_row * rows_per_shelf * shelves_per_closet
    result = cans_per_closet
    return result

print(solution())