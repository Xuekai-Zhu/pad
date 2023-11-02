def solution():
    # Find the number of thumbtacks used in one board
    thumbtacks_per_board = 3

    # Find the number of thumbtacks used in 120 boards
    total_thumbtacks_used = thumbtacks_per_board * 120

    # Find the number of thumbtacks left in one can
    thumbtacks_per_can_left = 30

    # Find the total number of thumbtacks left in all three cans
    total_thumbtacks_left = thumbtacks_per_can_left * 3

    # Find the total combined number of thumbtacks from the three full cans
    total_thumbtacks = total_thumbtacks_used + total_thumbtacks_left
    result = total_thumbtacks
    return result

print(solution())