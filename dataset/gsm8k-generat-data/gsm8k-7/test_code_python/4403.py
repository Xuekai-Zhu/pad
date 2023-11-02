def solution():
    num_friends = 4
    manny_portion = 1
    aaron_portion = 0
    kai_portion = 2 * manny_portion
    raphael_portion = 0.5 * manny_portion
    lisa_portion = 2

    # Calculate the total number of portions required
    total_portions = manny_portion + aaron_portion + kai_portion + raphael_portion + lisa_portion

    # Add extra portions for leftovers
    total_portions += total_portions * 0.1  # 10% extra

    # Round up to the nearest whole number
    num_pieces = int(total_portions + 0.5)

    result = num_pieces
    return result

print(solution())