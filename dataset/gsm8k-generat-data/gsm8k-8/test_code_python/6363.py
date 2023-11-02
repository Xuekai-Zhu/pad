def solution():
    # Convert player's height and reach to inches
    player_height = 6 * 12
    player_reach = player_height + 22

    # Calculate the minimum height the player needs to reach to dunk
    dunk_height = 10 + 6  # rim height + minimum reach above rim
    jump_height = dunk_height - player_reach

    result = jump_height
    return result

print(solution())