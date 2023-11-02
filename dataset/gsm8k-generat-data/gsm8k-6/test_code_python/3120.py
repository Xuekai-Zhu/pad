def solution():
    # Calculate the number of soaps in each box
    soaps_per_box = 192 * 6  # 6 packages per box, with 192 soaps per package

    # Calculate the total number of soaps in 2 boxes
    total_soaps = soaps_per_box * 2

    result = total_soaps
    return result

print(solution())