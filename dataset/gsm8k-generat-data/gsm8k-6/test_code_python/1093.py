def solution():
    # Calculate the total number of thumbtacks used in testing 120 boards
    thumbtacks_per_board = 3  # Lorenzo placed one thumbtack from each of the three cans into each board
    total_thumbtacks_used = thumbtacks_per_board * 120  # 120 boards tested
    remaining_thumbtacks_per_can = 30  # 30 tacks remaining in each can
    total_thumbtacks = total_thumbtacks_used + (remaining_thumbtacks_per_can * 3)  # 3 cans used in total
    result = total_thumbtacks
    return result

print(solution())