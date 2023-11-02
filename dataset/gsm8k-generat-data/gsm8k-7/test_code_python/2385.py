def solution():
    cans_per_row = 12
    rows_per_shelf = 4
    shelves_per_closet = 10

    # Calculate the total number of cans that can be stored on one shelf
    cans_per_shelf = cans_per_row * rows_per_shelf

    # Calculate the total number of cans that can be stored in one closet
    cans_per_closet = cans_per_shelf * shelves_per_closet
    result = cans_per_closet
    return result

print(solution())