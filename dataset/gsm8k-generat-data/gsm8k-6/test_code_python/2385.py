def solution():
    # Calculate the total number of cans that can be stored in one closet
    cans_per_shelf = 12 * 4  # 12 cans in one row and 4 rows on one shelf
    total_cans = cans_per_shelf * 10  # 10 shelves in one closet
    result = total_cans
    return result

print(solution())