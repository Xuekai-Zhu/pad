def solution():
    num_players = 5
    num_rounds = 6
    starting_blocks = 54

    # Calculate the total number of blocks removed in the first 5 rounds
    blocks_removed = num_rounds * num_players

    # Calculate the current number of blocks remaining after the first 5 rounds
    current_blocks = starting_blocks - blocks_removed

    # Subtract 1 for Jess's father's turn and 1 more for Jess's turn
    num_blocks_before_Jess = current_blocks - 2
    result = num_blocks_before_Jess
    return result

print(solution())