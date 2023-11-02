def solution():
    """Jack is trying to stack cans in his emergency bunker. If he can fit 12 cans in one row, 4 rows on one shelf, and 10 shelves in one closet, how many cans can he store in each closet?"""
    # Define the number of cans per row, number of rows per shelf, and number of shelves per closet
    cans_per_row = 12
    rows_per_shelf = 4
    shelves_per_closet = 10

    # Calculate the total number of cans that can be stored in one closet
    cans_per_closet = cans_per_row * rows_per_shelf * shelves_per_closet

    # Return the result
    result = cans_per_closet
    return result

print(solution())