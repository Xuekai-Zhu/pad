def solution():
    # Calculate the length of the board before the first cut
    initial_length = 143 + 25

    # Calculate the length of the board after the second cut
    final_length = initial_length - 7

    # Calculate the length of the other boards before the second cut
    other_board_length = final_length + 7

    # Calculate the length of the other boards before the first cut
    initial_board_length = other_board_length + 7

    # Return the initial length of the board
    result = initial_board_length
    return result

print(solution())