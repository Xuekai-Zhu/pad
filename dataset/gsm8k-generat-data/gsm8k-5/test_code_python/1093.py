def solution():
    boards_tested = 120  # Lorenzo tested 120 cork boards
    remaining_tacks = 30  # Lorenzo had 30 tacks remaining in each of the three cans
    tacks_per_board = 3  # Lorenzo used one thumbtack from each can for each board tested

    # Calculate the total number of thumbtacks used
    total_tacks = boards_tested * tacks_per_board

    # Calculate the total number of thumbtacks in the three cans
    total_tacks_in_cans = total_tacks + (3 * remaining_tacks)

    result = total_tacks_in_cans
    return result

print(solution())