def solution():
    cans_per_row = 12  # Jack can fit 12 cans in one row
    rows_per_shelf = 4  # Jack can fit 4 rows on one shelf
    shelves_per_closet = 10  # Jack can fit 10 shelves in one closet

    # Calculate the total number of cans that can be stored in one closet
    cans_per_closet = cans_per_row * rows_per_shelf * shelves_per_closet
    result = cans_per_closet
    return result

print(solution())