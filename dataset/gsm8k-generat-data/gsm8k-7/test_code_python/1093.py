def solution():
    num_tacks_per_board = 3
    num_boards_tested = 120
    num_tacks_remaining = 30

    # Calculate the total number of thumbtacks used in testing
    total_tacks_used = num_tacks_per_board * num_boards_tested

    # Calculate the total number of thumbtacks remaining in the three cans
    total_tacks_remaining = num_tacks_remaining * 3

    # Calculate the total combined number of thumbtacks from the three full cans
    total_tacks = total_tacks_used + total_tacks_remaining
    result = total_tacks
    return result

print(solution())